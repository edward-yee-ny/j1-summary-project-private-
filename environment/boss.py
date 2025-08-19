from .battle import BattleRoom

class BossRoom(BattleRoom):
    def __init__(self, name):
        super().__init__(name)
        self.room_type = "boss"
        self.description = "You are in the boss room. Defeat the boss to win the game!"
        self.battle_type = 'boss'
        
    def display(self):
        super().display()
        
        