# importing
from environment.map import *
from objects.item import Item 
from entities.player import Player
from environment.boss import BossRoom
from helper.extract_json import extractJson
from time import sleep
import json
import os
from helper.pack_json import packJson
from helper.typer import *


BATTLE_OUTCOMES = extractJson('data/battle_outcome.json')
DAMAGE_REPORT = extractJson('data/damage_report.json')

    # initialising
# add in the basic options, want to start the game or not (strat game load game quit)
game = Map()
player = Player()
game_over = False
def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    if os.name == 'nt':  # Check if the operating system is Windows
        os.system('cls')
    else:  # Assume Unix-like system (Linux, macOS)
        os.system('clear')

print("""
 ___                                ___     _    _                                               _   _                   _      _   
|  _`\  _                         /'___)   ( )_ ( )              /'\\_/`\                        ( ) ( )        _        ( )    ( )_ 
| (_) )(_)  ___    __        _   | (__     | ,_)| |__     __     |     |   __     __     _ _    | |/'/'  ___  (_)   __  | |__  | ,_)
| ,  / | |/',__) /'__`\    /'_`\ | ,__)    | |  |  _ `\ /'__`\   | (_) | /'__`\ /'_ `\ /'_` )   | , <  /' _ `\| | /'_ `\|  _ `\| |  
| |\ \ | |\\__, \(  ___/   ( (_) )| |       | |_ | | | |(  ___/   | | | |(  ___/( (_) |( (_| |   | |\`\ | ( ) || |( (_) || | | || |_ 
(_) (_)(_)(____/`\\____)   `\\___/'(_)       `\\__)(_) (_)`\\____)   (_) (_)`\\____)`\\__  |`\\__,_)   (_) (_)(_) (_)(_)`\\__  |(_) (_)`\\__)
                                                                               ( )_) |                           ( )_) |            
                                                                                \\___/'                            \\___/'            
""")
write_effect(f"""STAGE 1: Preliminary Rounds \nComplete these rounds to advance further in the tournament""", False)
=======

choice_load_or_new = input("""
Welcome to the game, what would you like to do.
1. New Game
2. Load Game
Key in the number :
""")
if choice_load_or_new == "1":
    pass
else:
    for i in extractJson("save_state.json")["moves"]:
        if i == "forward":
            game.go_forward()
            clear_terminal()
        elif i == "right":
            game.go_right()
            clear_terminal()
        else:
            game.go_left
            clear_terminal()
        clear_terminal()

print(f"""
STAGE 1: Preliminary Rounds \nComplete these rounds to advance further in the tournament""")
# functions used
def prompt_room_choice():
    """
    handles the room choice and moves into the room selected
    handles the choice to save game data
    """
    while True:
        choice = write_effect("Key in your choice of 1,2,3,4, or 5: ", True)
        if choice == "1": # left
            game.go_left()
            break
        elif choice == "2": # middle
            game.go_forward()
            break
        elif choice == "3": # right
            game.go_right()
            break
        elif choice == "4": # equip equipment
            # allows the player ot equip the equipment of their choice
            player.open_inventory()
            try:
                CHOICE = int(input(f"Input the index of the equipment to equip (1-indexed): "))-1
                player.update_equipment(player.inventory[CHOICE])
                write_effect(f"Item {player.inventory[CHOICE]} has been equipped successfully!", False)
            except Exception as e:
                write_effect("Invalid input.", False)
            
        
        elif choice == "5": # save game
            file_path = "save_state.json"
            
            write_effect("\nAttempting to save the game... (MK admires your patience!)", False)
            with open(file_path, "w") as f:
                json.dump({"moves" : game.direction_save_arr}, f)
            
            break
        else:
            write_effect("'WHERE IS THAT?' ~Mega Knight", False)
    return None

def fight(enemy):
    player.reset_hp()
    game_over = False

    # fighting loop
    while not game_over:
        
        player.display_stats()
        enemy.display_stats()
        
        sleep(1.4)

        action = input("\nwhat action do you take: \n 1. attack \n 2. open inventory \ninput your choice: ")
        
        print('')
        if action == "1": # player attack the enemy
            multi, damage = player.calculate_atk()
            enemy.update_hp(-damage)
            
            if multi > 1:
                write_effect("Megaknight feels a crit!", False)
                write_effect(DAMAGE_REPORT['Damage_Report']['Description'].replace("(multiplier)", str(multi)), False)
            write_effect(DAMAGE_REPORT['Damage_Report']['Damage_Dealt'].replace("(dmg)", str(damage)), False)
            sleep(0.6)

            if enemy.hp <= 0:
                write_effect(f"\n{BATTLE_OUTCOMES['Victory']}", False)
                # gives and autoequips the reward item for the player
                reward = game.currentRoom.reward
                player.update_inventory(reward)
                write_effect("MEGAKNIGHT: I should really equip something!", False)
                break
            # enemy attack the player
            if player.calculate_dmg(enemy.atk):
                write_effect(f"\n{BATTLE_OUTCOMES["Defeat"]}\n{BATTLE_OUTCOMES["Consolation"]}", False)
                exit(1)
            
            write_effect(DAMAGE_REPORT['Opponent_Action']['Description'].replace("(dmg)", str(enemy.atk)), False)

        elif action == "2":
            player.open_inventory()
        else:
            write_effect("MEGAKNIGHT CANNOT FOLLOW YOUR COMMAND.", False)
        
        sleep(0.6)

def battle_sequence(battle_type):
    # initialising necessary variables
    if battle_type == "normal":
        enemy = game.currentRoom.enemy
        fight(enemy)
    elif battle_type == "elite":
        enemy1 = game.currentRoom.enemy
        enemy2 = game.currentRoom.enemy2
        fight(enemy1)
        fight(enemy2)
    else:
        boss = game.currentRoom.enemy
        fight(boss)

    return None

def get_room_type():
    """returns the type of room player currently is in"""
    return game.currentRoom.room_type

def handle_room_action(room_type):
    """depending on the type of room carries out the appropriate actions"""

    if room_type == "treasure":
        reward = game.currentRoom.item
        player.update_inventory(reward)
        print("\nA new item has been added into your inventory!")
        player.update_equipment(reward)
        player.open_inventory()
    else:
        battle_sequence(room_type)


# intro
write_effect("Welcome to the arena.\nYou will assist Mega knight in competing in the tournament\nWinning each battle will give you an opportunity to choose your next opponent.\nBest of luck player", False)

# initial description of the starting room
game.displayCurrentRoom()
game.currentRoom.isCompleted = True

#game running code
while not game_over:
    # display possible paths
    print("Pick a direction to move in \n 1. Left \n 2. Middle \n 3. Right \n 4. Equip equipment \n 5. Save")
    
    # get the choice and move into the chosen room
    prompt_room_choice()

    # check room type, handle room actions
    if not game.currentRoom.isCompleted:
        room_type = get_room_type()
        handle_room_action(room_type)
        game.currentRoom.isCompleted = True
    
    # If it's a BossRoom completed, end the game.
    if isinstance(game.currentRoom, BossRoom):
        game_over = True

write_effect("\nYou have completed the dungeon!! :)\nWe hope you come back again...",False)