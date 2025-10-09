"""Helper functions for user input and validation."""

import random
from typing import Any


def roll_chance(chance: float) -> bool:
    """Rolls a random chance and returns True if successful.
    
    Args:
        chance (float): A float between 0 and 1 representing the chance of
        success.
    
    Returns:
        bool: True if the roll is successful, False otherwise.
    """
    return random.random() < chance


def prompt_valid_choice(
        preamble: str,
        options: list[str] | dict[str, Any],
        prompt: str="Your choice: "
) -> Any:
    """
    Prompts the user to make a valid choice.

    Args:
        preamble (str): Information to display to the user before the options.
        options (list or dict): A list of options or a dictionary where keys are valid choices and values are descriptions.
        prompt (str): The prompt to display when asking for input. Defaults to "Your choice: ".

    Returns:
        str or any: The valid choice made by the user. If options is a list, returns the selected item. If options is a dict, returns the value corresponding to the selected key.
    """
    print(preamble)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input(prompt)
    while not choice.isdecimal() or not 0 < int(choice) <= len(options):
        print("Invalid choice. Please try again.")
        choice = input(prompt)

    if isinstance(options, list):
        return options[int(choice) - 1]
    elif isinstance(options, dict):
        key = list(options.keys())[int(choice) - 1]
        return options[key]
    else:
        raise TypeError(
            f"options must be list or dict, got {type(options)}"
        )
