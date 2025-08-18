# importing
from environment.map import *
from objects.item import Item 

# initialising functions
dungeon = Map()




# functions used
def battle_sequence():
    return None



# intro
print("Welcome to the arena.",'\n', "You will assist Mega knight in competing in the tournament", '\n', "Winning each battle will give you an opportunity to choose your next opponent.", '\n', "Best of luck player")

# initial description of the starting room
dungeon.displayCurrentRoom()

#game running code
while True:
    # display possible paths
    print("Pick a direction to move in", "\n", "1. Left", "\n", "2. Middle", "\n", "3. Right")
    
    # get the choice and move into the chosen room
    check = True
    while check:
        choice = input("Key in your choice of 1,2 or 3: ")
        if choice == "1":
            check = not dungeon.go_left()
        elif choice == "2":
            check = not dungeon.go_forward()
        elif choice == "3":
            check = not dungeon.go_right()
        else:
            print("Invalid input")
    # check room type, handle room actions
    room_type = dungeon.currentRoom.room_type

    # - treasure room
    # - battle room
    handle_room_action()
    # run a for loop to display the possible options for moving to next room
    choice = prompt_room_choice()
    # pick next room
    move_to_room(choice)