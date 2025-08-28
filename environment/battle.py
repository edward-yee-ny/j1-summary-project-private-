from .room import Room
from helper.extract_json import extractJson
class BattleRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.room_type = "battle"
        self.description = extractJson('data/room_description.json')["room_des"]["battle_room"]
        self.enemy = None
        self.battle_type = 'normal'
        self.reward = None
        
    def display(self):
        super().display()
        print(f"Enemy: {self.enemy}")
        print(f"Battle Type: {self.battle_type}")
        print(f"Reward: {self.reward}")    