from .room import Room

class TreasureRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.item = None
        self.room_type = "treasure"
        self.description = "You are in a treasure room."
        
    def get_reward(self):
        return self.items if self.items else "No items available."
        
    def display(self):
        super().display()
        print(f"Item: {self.item}")
