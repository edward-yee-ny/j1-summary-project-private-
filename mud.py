# importing
from environment.map import *
from objects.item import Item 
from entities.player import Player
from environment.boss import BossRoom
from helper.extract_json import extractJson
from time import sleep
import json
from helper.pack_json import packJson

def open_and_dict(filename):
    with open(filename, 'r') as f:
        data = f.read()
    res = extractJson(data)
    return res

BATTLE_OUTCOMES = open_and_dict('data/battle_outcome.json')
DAMAGE_REPORT = open_and_dict('data/damage_report.json')
class Game:
    def __init__(self):
        self.game = Map()
        self.player = Player()
        self.game_over = False
        self.choice = input("""
                Welcome to the game, what would you like to do.
                1. New Game
                2. Load Game
                Key in the number :
        """)
    def rungame(self, game, player, game_over):

        BATTLE_OUTCOMES = open_and_dict('data/battle_outcome.json')
        DAMAGE_REPORT = open_and_dict('data/damage_report.json')

        print("""
        ___                                ___     _    _                                               _   _                   _      _   
        |  _`\\  _                         /'___)   ( )_ ( )              /'\_/`\                        ( ) ( )        _        ( )    ( )_ 
        | (_) )(_)  ___    __        _   | (__     | ,_)| |__     __     |     | \ ___    __     _ _   | |/'/'  ___  (_)   __  | |__  | ,_)
        | ,  / | |/',__) /'__`\    /'_`\ | ,__)    | |  |  _ `\ /'__`\   | (_) | /'__`\ /'_ `\ /'_` )   | , <  /' _ `\| | /'_ `\|  _ `\| |  
        | |\ \ | |\__, \(  ___/   ( (_) )| |       | |_ | | | |(  ___/   | | | |(  ___/( (_) |( (_| |   | |\`\ | ( ) || |( (_) || | | || |_ 
        (_) (_)(_)(____/`\____)   `\___/'(_)       `\__)(_) (_)`\____)   (_) (_)`\____)`\__  |`\__,_)   (_) (_)(_) (_)(_)`\__  |(_) (_)`\__)
                                                                                    ( )_) |                           ( )_) |            
                                                                                        \___/'                            \___/'            
        """)
        print(f"""
        STAGE 1: Preliminary Rounds \nComplete these rounds to advance further in the tournament""")
        # functions used
        def prompt_room_choice():
            """
            handles the room choice and moves into the room selected
            handles the choice to save game data
            """
            while True:
                choice = input("Key in your choice of 1,2,3,4, or 5: ")
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
                        print(f"Item {player.inventory[CHOICE]} has been equipped successfully!")
                    except Exception as e:
                        print("Invalid input.")
                    
                
                elif choice == "5": # save game
                    file_path = "save_state.json"
                    
                    print("\nAttempting to save the game... (MK admires your patience!)")
                    with open(file_path, "w") as f:
                        json.dump({"moves" : game.direction_save_arr}, f)
                    
                    break
                else:
                    print("'WHERE IS THAT?' ~Mega Knight")
            return None

        def fight(enemy):
            player.reset_hp()
            game_over = False

            # fighting loop
            while not game_over:
                
                player.display_stats()
                enemy.display_stats()
                
                sleep(1.4)

                action = input("\n what action do you take \n 1. attack \n 2. open inventory \n input your choice: ")
                
                print('')
                if action == "1": # player attack the enemy
                    multi, damage = player.calculate_atk()
                    enemy.update_hp(-damage)
                    
                    if multi > 1:
                        print("Megaknight feels a crit!")
                        print(DAMAGE_REPORT['Damage_Report']['Description'].replace("(multiplier)", str(multi)))
                    print(DAMAGE_REPORT['Damage_Report']['Damage_Dealt'].replace("(dmg)", str(damage)))
                    sleep(0.6)

                    if enemy.hp <= 0:
                        print("\n", BATTLE_OUTCOMES['Victory'])
                        # gives and autoequips the reward item for the player
                        reward = game.currentRoom.reward
                        player.update_inventory(reward)
                        print("MEGAKNIGHT: I should really equip something!")
                        break
                    # enemy attack the player
                    if player.calculate_dmg(enemy.atk):
                        print("\n", BATTLE_OUTCOMES["Defeat"], '\n', BATTLE_OUTCOMES["Consolation"])
                        exit(1)
                    
                    print(DAMAGE_REPORT['Opponent_Action']['Description'].replace("(dmg)", str(enemy.atk)))

                elif action == "2":
                    player.open_inventory()
                else:
                    print("MEGAKNIGHT CANNOT FOLLOW YOUR COMMAND.")
                
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
                print("\n", "A new item has been added into your inventory!")
                player.update_equipment(reward)
                player.open_inventory()
            else:
                battle_sequence(room_type)


        # intro
        print("Welcome to the arena.",'\n', "You will assist Mega knight in competing in the tournament", '\n', "Winning each battle will give you an opportunity to choose your next opponent.", '\n', "Best of luck player")

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

        print("\n You have completed the dungeon!! :)","\n","We hope you come back again...")
    if choice == "1":
        self.rungame(self.game, self.player, self.game_over)
    elif choice == "2":
        current = self.game.currentRoom
        for i in open_and_dict("save_state.json")["moves"]:
            if i == "forward":
                current = current.forward
            elif i == "right":
                current = current.right
            else:
                current = current.left
game = Game()
