# importing
from environment.map import *
from entities.player import Player
from environment.boss import BossRoom
from helper.extract_json import extractJson
from time import sleep
import json

from helper import prompt_valid_choice

from . import text

BATTLE_OUTCOMES = extractJson('data/battle_outcome.json')
DAMAGE_REPORT = extractJson('data/damage_report.json')
SAVE_FILE_PATH = "save_state.json"

class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.game_over = False
        self.choice = prompt_valid_choice(
            "Welcome to the game, what would you like to do?",
            text.GAME_MENU_OPTIONS,
        )

    def handle_equip_choice(self, choice: str) -> None:
        """Handles the equipment choice and equips the selected item."""
        self.player.update_equipment(self.player.inventory[self.player.inventory.index(choice)])
        print(f"Item {choice} has been equipped successfully!")

    def handle_battle(self, battle_type) -> None:
        """Handles the battle sequence based on the type of battle."""
        # initialising necessary variables
        if battle_type == "normal":
            enemy = self.map.currentRoom.enemy
            self.handle_fight(enemy)
        elif battle_type == "elite":
            enemy1 = self.map.currentRoom.enemy
            enemy2 = self.map.currentRoom.enemy2
            self.handle_fight(enemy1)
            self.handle_fight(enemy2)
        else:
            boss = self.map.currentRoom.enemy
            self.handle_fight(boss)

    def handle_fight(self, enemy) -> None:
        self.player.reset_hp()
        self.game_over = False

        # fighting loop
        while not self.game_over:
            self.player.display_stats()
            enemy.display_stats()
            sleep(1.4)

            action = prompt_valid_choice(
                preamble="What action do you take?",
                options=text.FIGHT_MENU_OPTIONS,
            )
            print('')

            if action == text.OPTION_ATTACK:
                self.handle_fight_attack(enemy)
            elif action == text.OPTION_OPEN_INVENTORY:
                self.player.display_inventory()

            sleep(0.6)

    def handle_fight_attack(self, enemy) -> None:
        """Handles the fight attack sequence between the player and the enemy."""
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
            return
        # enemy attack the player
        if self.player.calculate_dmg(enemy.atk):
            print("\n", BATTLE_OUTCOMES["Defeat"], '\n', BATTLE_OUTCOMES["Consolation"])
            exit(1)

        print(DAMAGE_REPORT['Opponent_Action']['Description'].replace("(dmg)", str(enemy.atk)))

    def handle_menu_choice(self, choice: str) -> None:
        """Handles the room choice and moves into the room selected.
        Handles the choice to save game data.
        """
        if choice == text.OPTION_GO_LEFT:
            self.map.go_left()
        elif choice == text.OPTION_GO_FORWARD:
            self.map.go_forward()
        elif choice == text.OPTION_GO_RIGHT:
            self.map.go_right()
        elif choice == text.OPTION_EQUIP_EQUIPMENT:
            self.player.display_inventory()
            equip_choice = prompt_valid_choice(
                preamble="Select equipment to equip.",
                options=[str(item) for item in self.player.inventory],
            )
            self.handle_equip_choice(equip_choice)
        elif choice == text.OPTION_SAVE_GAME:
            self.handle_savegame()

    def handle_room_choice(self, room_type) -> None:
        """Handles the room choice and the actions within the room."""
        if room_type == "treasure":
            reward = self.map.currentRoom.item
            self.player.update_inventory(reward)
            print("\n", "A new item has been added into your inventory!")
            self.player.update_equipment(reward)
            self.player.display_inventory()
        else:
            self.handle_battle(room_type)

    def handle_savegame(self) -> None:
        """Saves the current game state to a JSON file."""
        print(text.MSG_SAVE_GAME)
        with open(SAVE_FILE_PATH, "w") as f:
            json.dump({"moves": self.map.direction_save_arr}, f)

    def run(self) -> None:
        # functions used
        def get_room_type():
            """returns the type of room player currently is in"""
            return self.map.currentRoom.room_type

        # intro
        print(text.load_textfile(text.INTRO_FILE))

        # initial description of the starting room
        self.map.displayCurrentRoom()
        self.map.currentRoom.isCompleted = True

        # main loop
        while not self.game_over:
            choice = prompt_valid_choice(
                "Choose your next action:",
                text.MAIN_MENU_OPTIONS,
            )
            self.handle_menu_choice(choice)

            # check room type, handle room actions
            if not self.map.currentRoom.isCompleted:
                room_type = get_room_type()
                self.handle_room_choice(room_type)
                self.map.currentRoom.isCompleted = True

            # If it's a BossRoom completed, end the game.
            if isinstance(self.map.currentRoom, BossRoom):
                self.game_over = True

        print(text.load_textfile(text.OUTRO_FILE))

if __name__ == "__main__":
    game = Game()
    game.run()
