from environment.room import Room

class TreasureRoom(Room):
    def __init__(self):
        super().__init__()
        self.items = []
        
    def get_items(self):
        pass
        
    def add_item(self, item):
        pass