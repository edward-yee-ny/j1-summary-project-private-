from environment.room import Room

class TreasureRoom(Room):
    def __init__(self):
        super().__init__()
        self.items = []
        
        