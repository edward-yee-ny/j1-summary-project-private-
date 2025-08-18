from .room import Room

class BattleRoom(Room):
    def __init__(self):
        super().__init__()
        self.room_type = "battle"
        self.description = "You are in a battle room."
        self.enemy = None
        self.battle_type = 'normal'
        self.reward = None
        
    def display(self):
        super().display()
        print(f"Enemy: {self.enemy}")
        print(f"Battle Type: {self.battle_type}")
        print(f"Reward: {self.reward}")    