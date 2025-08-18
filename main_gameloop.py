# importing
from environment.map import *
from objects.item import Item 
from entities.player import Player

# initialising
game = Map()
player = Player()
game_over = False


# functions used
def prompt_room_choice():
    check = True
    while check:
        choice = input("Key in your choice of 1,2 or 3: ")
        if choice == "1":
            check = not game.go_left()
        elif choice == "2":
            check = not game.go_forward()
        elif choice == "3":
            check = not game.go_right()
        else:
            print("Invalid input")
    return choice


def battle_sequence():
    # initialising necessary variables
    enemy = currentRoom.enemy
    player.reset_hp
    game.currentRoom.display()

    # fighting loop
    while True:
        enemy.display_stats()
        action = input("what action do you take", "\n", "1. attack", "\n", "2. open inventory")
        
        if action == "1": # player attack the enemy
            damage = player.calculate_atk
            enemy.update_hp(-damage)
            if enemy.hp <= 0:
                print("\n", "congrats you win")
                # gives and autoequips the reward item for the player
                reward = game.currentRoom.reward
                player.update_inventory(reward)
                player.update_equipment(reward)
                break
        if action == "2":
            player.open_inventory()
            # for now this is all it does

        # enemy attack the player
        player.update_hp(-enemy.atk)
        if player.hp <= 0:
            print("\n", "game over")
            game_over = True
    
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

print("ByeBye!! :)")