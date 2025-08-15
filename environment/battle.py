from room import Room

class BattleRoom(Room):
    def __init__(self):
        super().__init__()
        self.description = "You are in a battle room."
        self.enemy = None
        self.battle_type = None
        self.reward = None
        
    def display(self):
        super().display()
    
    def get_reward(self):
        pass
    
    def get_attack(self):
        pass
        
        