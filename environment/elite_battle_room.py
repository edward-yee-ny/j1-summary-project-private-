from .battle import BattleRoom
from helper.extract_json import extractJson
class EliteBattleRoom(BattleRoom):
    """Contains 2 elite enemies that have to be defeated to proceed."""
    def __init__(self, name):
        super().__init__(name)
        self.room_type = "elite"
        self.description = extractJson('data/room_description.json')["room_des"]["elite_room"]
"""
        self.battle_type = 'elite'
        self.reward2 = None
        self.enemy2 = None
        
    def display(self):
        print(self.description)
        print(f"Battle Type: {self.battle_type}")
        print(f"Enemy 1: {self.enemy}")
        print(f"Reward 1: {self.reward}")
        print(f"Enemy 2: {self.enemy2}")
        print(f"Reward 2: {self.reward2}")"""
