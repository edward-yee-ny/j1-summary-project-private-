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
|  _`\\  _                         /'___)   ( )_ ( )              /'\_/`\                        ( ) ( )        _        ( )    ( )_ 
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
        print("\n")
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
            print("Invalid input \n")
    return choice

def fight(enemy):
    player.reset_hp()
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
                exit_ = input("\n exit? \n key in y to exit: ")
                if exit_ == "y":
                    break

def battle_sequence(battle_type):
    # initialising necessary variables
    if battle_type == "normal":
        enemy = game.currentRoom.enemy
        print(enemy)
        fight(enemy)
    elif battle_type == "elite":
        enemy1 = game.currentRoom.enemy1
        enemy2 = game.currentRoom.enemy2
        fight(enemy1)
        f
        :
  wewgame        boss =boss.currentRoom.enemy
        fight(enemy)

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

#game running code
while not game_over:
    # display possible paths
    print("Pick a direction to move in \n 1. Left \n 2. Middle \n 3. Right")
    
    # get the choice and move into the chosen room
    choice = prompt_room_choice()

    # check room type, handle room actions
    room_type = get_room_type()
    handle_room_action(room_type)

    # - treasure room
    # - battle room

print("ByeBye!! :)","\n","please try again")