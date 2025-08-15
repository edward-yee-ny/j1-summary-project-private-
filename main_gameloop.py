# importing
from environment.map import *
from objects.item import Item 

# functions used
def battle_sequence():
    

def display_current_room():
    







#intro
print(f"Welcome to the arena.,'/n', You will assist Mega knight in competing in the tournament, '/n', Winning each battle will give you an opportunity to choose your next opponent., '/n', Best of luck player)


map = Map()
display_current_room()



#game running code
while true:
    room_description = map.
    print(f"you are in the {#insert room description here} room")
    for i in range(3):
        # display room name, descrition

    
    display_current_room()
    
    # check room type, handle room actions
    # - treasure room
    # - battle room
    handle_room_action()
    # run a for loop to display the possible options for moving to next room
    choice = prompt_room_choice()
    # pick next room
    move_to_room(choice)