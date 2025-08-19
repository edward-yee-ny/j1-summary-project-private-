from .battle import BattleRoom

class EliteBattleRoom(BattleRoom):
    """Contains 2 elite enemies that have to be defeated to proceed."""
    def __init__(self):
        super().__init__()
        self.room_type = "elite"
        self.description = "You are in an elite battle room with two formidable enemies."
        self.battle_type = 'elite'
        self.reward2 = None
        self.enemy2 = None
        
    def display(self):
        print(self.description)
        print(f"Battle Type: {self.battle_type}")
        print(f"Enemy 1: {self.enemy}")
        print(f"Reward 1: {self.reward}")
        print(f"Enemy 2: {self.enemy2}")
        print(f"Reward 2: {self.reward2}")
