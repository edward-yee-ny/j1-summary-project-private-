from room import Room

class TreasureRoom(Room):
    def __init__(self):
        super().__init__()
        self.items = []
        self.description = "You are in a treasure room."
        
    def get_items(self):
        pass
        
    def display(self):
        super().display()
