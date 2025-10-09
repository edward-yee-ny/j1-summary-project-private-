"""Module for handling text files and game menu options."""

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

def load_textfile(filename: str) -> str:
    """Loads and returns the content of a text file."""
    with open(filename, "r") as file:
        return file.read()
