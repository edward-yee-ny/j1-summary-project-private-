from .room import Room

class TreasureRoom(Room):
    def __init__(self):
        super().__init__()
        self.item = None
        self.room_type = "treasure"
        self.description = "You are in a treasure room."
        
    def display(self):
        """displays the item assigned to the room"""
        super().display()
        print(f"Item: {self.item}")
