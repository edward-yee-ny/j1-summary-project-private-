# importing
from environment.map import *
from entities.player import Player
from environment.boss import BossRoom
from helper.extract_json import extractJson
from time import sleep
import json

from helper import prompt_valid_choice

# Define a global constant for the intro file
INTRO_FILE = "intro.txt"
OUTRO_FILE = "outro.txt"
OPTION_NEW_GAME = "New Game"
OPTION_LOAD_GAME = "Load Game"
OPTION_GO_LEFT = "Go Left"
OPTION_GO_FORWARD = "Go Forward"
OPTION_GO_RIGHT = "Go Right"
OPTION_EQUIP_EQUIPMENT = "Equip Equipment"
OPTION_SAVE_GAME = "Save Game"
OPTION_ATTACK = "Attack"
OPTION_OPEN_INVENTORY = "Open Inventory"
GAME_MENU_OPTIONS = [
    OPTION_NEW_GAME,
    OPTION_LOAD_GAME
]
MAIN_MENU_OPTIONS = [
    OPTION_GO_LEFT,
    OPTION_GO_FORWARD,
    OPTION_GO_RIGHT,
    OPTION_EQUIP_EQUIPMENT,
    OPTION_SAVE_GAME
]
FIGHT_MENU_OPTIONS = [
    OPTION_ATTACK,
    OPTION_OPEN_INVENTORY
]
BATTLE_OUTCOMES = extractJson('data/battle_outcome.json')
DAMAGE_REPORT = extractJson('data/damage_report.json')

def load_textfile(filename):
    """Loads the content of a text file."""
    with open(filename, "r") as file:
        return file.read()

class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.game_over = False
        self.choice = prompt_valid_choice(
            "Welcome to the game, what would you like to do?",
            GAME_MENU_OPTIONS,
        )

    def run(self):
        print(load_textfile(INTRO_FILE))
        # functions used
        def handle_menu_choice(choice: str):
            """Handles the room choice and moves into the room selected.
            Handles the choice to save game data.
            """
            if choice == OPTION_GO_LEFT:
                self.map.go_left()
            elif choice == OPTION_GO_FORWARD:
                self.map.go_forward()
            elif choice == OPTION_GO_RIGHT:
                self.map.go_right()
            elif choice == OPTION_EQUIP_EQUIPMENT:
                self.player.open_inventory()
                try:
                    equip_choice = prompt_valid_choice(
                        preamble="Select equipment to equip.",
                        options=[str(item) for item in self.player.inventory],
                    )
                    self.player.update_equipment(self.player.inventory[self.player.inventory.index(equip_choice)])
                    print(f"Item {equip_choice} has been equipped successfully!")
                except Exception as e:
                    print("Invalid input.")
            elif choice == "Save Game":
                file_path = "save_state.json"
                print("\nAttempting to save the game... (MK admires your patience!)")
                with open(file_path, "w") as f:
                    json.dump({"moves": self.map.direction_save_arr}, f)

        def fight(enemy):
            self.player.reset_hp()
            self.game_over = False

            # fighting loop
            while not self.game_over:

                self.player.display_stats()
                enemy.display_stats()

                sleep(1.4)

                action = prompt_valid_choice(
                    preamble="What action do you take?",
                    options=FIGHT_MENU_OPTIONS,
                )

                print('')
                if action == OPTION_ATTACK:  # player attack the enemy
                    multi, damage = self.player.calculate_atk()
                    enemy.update_hp(-damage)

                    if multi > 1:
                        print("Megaknight feels a crit!")
                        print(DAMAGE_REPORT['Damage_Report']['Description'].replace("(multiplier)", str(multi)))
                    print(DAMAGE_REPORT['Damage_Report']['Damage_Dealt'].replace("(dmg)", str(damage)))
                    sleep(0.6)

                    if enemy.hp <= 0:
                        print("\n", BATTLE_OUTCOMES['Victory'])
                        # gives and autoequips the reward item for the player
                        reward = self.map.currentRoom.reward
                        self.player.update_inventory(reward)
                        print("MEGAKNIGHT: I should really equip something!")
                        break
                    # enemy attack the player
                    if self.player.calculate_dmg(enemy.atk):
                        print("\n", BATTLE_OUTCOMES["Defeat"], '\n', BATTLE_OUTCOMES["Consolation"])
                        exit(1)

                    print(DAMAGE_REPORT['Opponent_Action']['Description'].replace("(dmg)", str(enemy.atk)))

                elif action == OPTION_OPEN_INVENTORY:
                    self.player.open_inventory()

                sleep(0.6)

        def battle_sequence(battle_type):
            # initialising necessary variables
            if battle_type == "normal":
                enemy = self.map.currentRoom.enemy
                fight(enemy)
            elif battle_type == "elite":
                enemy1 = self.map.currentRoom.enemy
                enemy2 = self.map.currentRoom.enemy2
                fight(enemy1)
                fight(enemy2)
            else:
                boss = self.map.currentRoom.enemy
                fight(boss)

            return None

        def get_room_type():
            """returns the type of room player currently is in"""
            return self.map.currentRoom.room_type

        def handle_room_action(room_type):
            """depending on the type of room carries out the appropriate actions"""

            if room_type == "treasure":
                reward = self.map.currentRoom.item
                self.player.update_inventory(reward)
                print("\n", "A new item has been added into your inventory!")
                self.player.update_equipment(reward)
                self.player.open_inventory()
            else:
                battle_sequence(room_type)


        # intro
        print(load_textfile(INTRO_FILE))

        # initial description of the starting room
        self.map.displayCurrentRoom()
        self.map.currentRoom.isCompleted = True

        #game running code
        while not self.game_over:
            choice = prompt_valid_choice(
                "Choose your next action:",
                MAIN_MENU_OPTIONS,
            )
            handle_menu_choice(choice)

            # check room type, handle room actions
            if not self.map.currentRoom.isCompleted:
                room_type = get_room_type()
                handle_room_action(room_type)
                self.map.currentRoom.isCompleted = True

            # If it's a BossRoom completed, end the game.
            if isinstance(self.map.currentRoom, BossRoom):
                self.game_over = True

        print(load_textfile(OUTRO_FILE))
