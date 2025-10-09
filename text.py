"""Module for handling text files and game menu options."""

from time import sleep

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

OUTCOME_VICTORY = "YOU HAVE DEFEATED THE OPPONENT"
OUTCOME_DEFEAT = "YOU HAVE BEEN DEFEATED"
OUTCOME_CONSOLATION = "Better luck next time"

MSG_PICKUP_ITEM = "MEGAKNIGHT: I should really equip something!"
MSG_SAVE_GAME = "Attempting to save the game... (MK admires your patience!)"

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


def divider() -> None:
    """Prints a divider for better readability."""
    print("-" * 40)

def linebreak() -> None:
    """Prints a line break for better readability."""
    print()

def wait_short() -> None:
    """Waits for a short duration."""
    sleep(0.6)

def wait_long() -> None:
    """Waits for a longer duration."""
    sleep(1.2)

def fight_report_crit(attacker: str, multiplier: float) -> None:
    """Reports a critical hit with the given multiplier."""
    print(f"{attacker} feels a crit!")
    print(f"Atk is enhanced by {multiplier}!")

def fight_report_damage(attacker: str, defender: str, damage: int) -> None:
    """Prints a report of damage dealt from attacker to defender."""
    print(f"{attacker} dealt {damage} damage to {defender}.")


def load_textfile(filename: str) -> str:
    """Loads and returns the content of a text file."""
    with open(filename, "r") as file:
        return file.read()
