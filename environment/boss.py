from room import Room

class BossRoom(Room):
    def __init__(self):
        super().__init__()
        self.description = "You are in the boss room."
        
    def display(self):
        super().display()
        
        