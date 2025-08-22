from .room import Room

class TreasureRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.item = None
        self.room_type = "treasure"
        self.description = "You are in a treasure room."
        
    def display(self):
        """displays the item assigned to the room"""
        super().display()
        print(f"Item: {self.item}")
