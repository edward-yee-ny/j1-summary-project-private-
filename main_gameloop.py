# importing
from environment.map import *
from objects.item import Item 
from entities.player import Player

# initialising
# add in the basic options, want to start the game or not (strat game load game quit)
game = Map()
player = Player()
game_over = False

print("""
 ___                                ___     _    _                                               _   _                   _      _   
|  _`\  _                         /'___)   ( )_ ( )              /'\_/`\                        ( ) ( )        _        ( )    ( )_ 
| (_) )(_)  ___    __        _   | (__     | ,_)| |__     __     |     |   __     __     _ _    | |/'/'  ___  (_)   __  | |__  | ,_)
| ,  / | |/',__) /'__`\    /'_`\ | ,__)    | |  |  _ `\ /'__`\   | (_) | /'__`\ /'_ `\ /'_` )   | , <  /' _ `\| | /'_ `\|  _ `\| |  
| |\ \ | |\__, \(  ___/   ( (_) )| |       | |_ | | | |(  ___/   | | | |(  ___/( (_) |( (_| |   | |\`\ | ( ) || |( (_) || | | || |_ 
(_) (_)(_)(____/`\____)   `\___/'(_)       `\__)(_) (_)`\____)   (_) (_)`\____)`\__  |`\__,_)   (_) (_)(_) (_)(_)`\__  |(_) (_)`\__)
                                                                               ( )_) |                           ( )_) |            
                                                                                \___/'                            \___/'            
""")
# functions used
def prompt_room_choice():
    while True:
        choice = input("Key in your choice of 1,2 or 3: ")
        if choice == "1":
            game.go_left()
            break
        elif choice == "2":
            game.go_forward()
            break
        elif choice == "3":
            game.go_right()
            break
        else:
            print("Invalid input")
    return choice


def battle_sequence():
    # initialising necessary variables
    enemy = game.currentRoom.enemy
    player.reset_hp()
    game.currentRoom.display()
    game_over = False

    # fighting loop
    while not game_over:
        player.display_stats()
        enemy.display_stats()

        action = input("\n what action do you take \n 1. attack \n 2. open inventory \n input your choice: ")
        
        if action == "1": # player attack the enemy
            damage = player.calculate_atk()
            enemy.update_hp(-damage)

            if enemy.hp <= 0:
                print("\n", "congrats you win")
                # gives and autoequips the reward item for the player
                reward = game.currentRoom.reward
                player.update_inventory(reward)
                player.update_equipment(reward)
                break
            # enemy attack the player
            if player.calculate_dmg(enemy.atk):
                print("\n", "game over")
                game_over = True

        if action == "2":
            player.open_inventory()
            while True:
                exit_ = input("exit? \n key in y to exit:")
                if exit_ == "y":
                    break
            # for now this is all it does
    
    return None

def get_room_type():
    """returns the type of room player currently is in"""
    return game.currentRoom.room_type

def handle_room_action(room_type):
    """depending on the type of room carries out the appropriate actions"""
    if room_type == "battle":
        battle_sequence()

    if room_type == "treasure":
        reward = game.currentRoom.item
        player.update_inventory(reward)
        game.currentRoom.display()
        print("\n", "a new item has been added into your inventory!")
        player.update_equipment(reward)

    if room_type == "boss":
        battle_sequence()


# intro
print("Welcome to the arena.",'\n', "You will assist Mega knight in competing in the tournament", '\n', "Winning each battle will give you an opportunity to choose your next opponent.", '\n', "Best of luck player")

# initial description of the starting room
game.displayCurrentRoom()

#game running code
while not game_over:
    # display possible paths
    print("Pick a direction to move in", "\n", "1. Left", "\n", "2. Middle", "\n", "3. Right")
    
    # get the choice and move into the chosen room
    choice = prompt_room_choice()

    # check room type, handle room actions
    room_type = get_room_type()
    handle_room_action(room_type)

    # - treasure room
    # - battle room

print("ByeBye!! :)","\n","please try again")