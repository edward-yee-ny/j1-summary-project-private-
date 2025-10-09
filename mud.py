# importing
from environment.map import *
from entities import Combatant, Player
from environment import BattleRoom, TreasureRoom, Room
from helper.extract_json import extractJson
from time import sleep
import json

from helper import prompt_valid_choice, random_between, roll_chance
from item import Item

from . import text

BATTLE_OUTCOMES = extractJson('data/battle_outcome.json')
DAMAGE_REPORT = extractJson('data/damage_report.json')
SAVE_FILE_PATH = "save_state.json"
PLAYER_HEALTH = 1750
PLAYER_ATTACK = 200
PLAYER_CRIT_CHANCE = 0.2
CRIT_THRESHOLD = 1.3  # multiplier threshold for crit message

class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player(
            name="Megaknight",
            hp=PLAYER_HEALTH,
            atk=PLAYER_ATTACK,
            crit_chance=PLAYER_CRIT_CHANCE
        )
        self.game_over = False
        self.choice = prompt_valid_choice(
            "Welcome to the game, what would you like to do?",
            text.GAME_MENU_OPTIONS,
        )

    def determine_attack_outcome(self,
                                 attacker: Combatant,
                                 defender: Combatant) -> dict:
        """Determines the outcome of an attack between two entities.
        
        Args:
            attacker: The entity initiating the attack.
            defender: The entity defending against the attack.
                      (for future use, e.g., armor/item effects)

        Returns:
            {
                "multiplier": float | int,
                "damage": int,
            }
        """
        if roll_chance(attacker.crit_chance):
            multiplier = 2
        else:
            multiplier = 1 + random_between(0, 0.5, dp=2)
        damage = self.calculate_damage(attacker)
        return {
            "multiplier": multiplier,
            "damage": damage,
        }

    def calculate_damage(self, attacker: Combatant) -> int:
        """Calculates the attack damage of a combatant."""
        weapon = attacker.get_weapon()
        if weapon:
            return 200 + weapon.atk
        else:
            return attacker.atk

    def handle_equip_choice(self, choice: str) -> None:
        """Handles the equipment choice and equips the selected item."""
        self.player.equip(self.player.inventory.get(choice))
        print(f"Item {choice} has been equipped successfully!")

    def handle_battle(self) -> None:
        """Handles the battle sequence based on the type of battle."""
        current_room = self.map.get_current_room()
        assert isinstance(current_room, BattleRoom)
        for enemy in current_room.get_enemies():
            self.handle_fight(enemy)

    def handle_fight(self, enemy: Enemy) -> None:
        """Handles the fight sequence between the player and a single enemy."""
        self.player.restore()
        self.game_over = False

        # fighting loop
        attacker = self.player
        defender = enemy
        victor = None
        while victor is None:
            attacker.display_stats()
            defender.display_stats()
            text.wait_long()
            if isinstance(attacker, Player):
                attacker_action = prompt_valid_choice(
                    preamble="What action do you take?",
                    options=text.FIGHT_MENU_OPTIONS,
                )
            else:
                attacker_action = text.OPTION_ATTACK

            if attacker_action == text.OPTION_ATTACK:
                victor = self.handle_fight_attack(attacker, defender)
            elif attacker_action == text.OPTION_OPEN_INVENTORY:
                attacker.display_inventory()
            text.wait_short()

            # swap roles
            attacker, defender = defender, attacker

        # Victor decided
        if isinstance(victor, Player):
            text.linebreak()
            print(text.OUTCOME_VICTORY)
            reward = self.handle_fight_reward()
            if reward:
                print(text.MSG_PICKUP_ITEM)
        else:
            text.linebreak()
            print(text.OUTCOME_DEFEAT)
            text.linebreak()
            print(text.OUTCOME_CONSOLATION)
            exit(1)


    def handle_fight_attack(self,
                            attacker: Combatant,
                            defender: Combatant) -> Combatant | None:
        """Handles the fight attack sequence between an attacker and defender.
        
        Player attacks first, then enemy attacks if still alive.
        Returns the victor (Player or Enemy).
        """
        outcome = self.determine_attack_outcome(attacker, defender)
        defender.take_damage(outcome["damage"])
        self.report_attack_outcome(attacker, defender, outcome)
        return attacker if defender.is_dead() else None

    def handle_fight_reward(self) -> list[Item]:
        """Handles the reward sequence after a fight."""
        room = self.map.get_current_room()
        assert isinstance(room, BattleRoom)
        reward = room.get_reward()
        if reward:
            for item in reward:
                self.player.update_inventory(item)
        return reward

    def report_attack_outcome(self,
                              attacker: Combatant,
                              defender: Combatant,
                              outcome: dict) -> None:
        """Handles the outcome of an attack."""
        multiplier = outcome["multiplier"]
        damage = outcome["damage"]
        if multiplier >= CRIT_THRESHOLD:
            text.fight_report_crit(attacker.name, multiplier)
        text.fight_report_damage(attacker.name, defender.name, damage)
        text.wait_short()

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

    def update_room(self) -> None:
        """Handles the room choice and the actions within the room."""
        current_room = self.map.get_current_room()
        if isinstance(current_room, TreasureRoom):
            reward = current_room.get_item()
            self.player.update_inventory(reward)
            print("\n", "A new item has been added into your inventory!")
            self.player.update_equipment(reward)
            self.player.display_inventory()
        elif isinstance(current_room, BattleRoom):
            self.handle_battle()
        current_room.set_complete()

    def handle_savegame(self) -> None:
        """Saves the current game state to a JSON file."""
        print(text.MSG_SAVE_GAME)
        with open(SAVE_FILE_PATH, "w") as f:
            json.dump({"moves": self.map.get_direction_history()}, f)

    def run(self) -> None:
        """Runs the main game loop."""
        # Reset map layout
        self.map.reset()

        # intro
        print(text.load_textfile(text.INTRO_FILE))

        # initial description of the starting room
        self.map.displayCurrentRoom()

        # main loop
        while not self.game_over:
            choice = prompt_valid_choice(
                "Choose your next action:",
                text.MAIN_MENU_OPTIONS,
            )
            self.handle_menu_choice(choice)

            # check room type, handle room actions
            current_room = self.map.get_current_room()
            if not current_room.isCompleted:
                self.update_room()
                current_room.set_complete()

            # If it's the final room, end the game.
            if current_room.is_last_room():
                self.game_over = True

        print(text.load_textfile(text.OUTRO_FILE))

if __name__ == "__main__":
    game = Game()
    game.run()
