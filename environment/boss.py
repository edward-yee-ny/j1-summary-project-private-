from .battle import BattleRoom
from helper.extract_json import extractJson
class BossRoom(BattleRoom):
    def __init__(self, name):
        super().__init__(name)
        self.room_type = "boss"
        
        self.description = extractJson('data/room_description.json')["room_des"]["boss_room"]
    def display(self):
        super().display()
        
        