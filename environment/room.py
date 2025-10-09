"""Room types for the game environment."""


class Room:
    def __init__(self,
                 name: str,
                 room_type: str,
                 description: str = ""):
        self.name = name
        self.description = description
        self.room_type = room_type
        self.right = None
        self.left = None
        self.forward = None
        self.visit_status = False
        self.isCompleted = False
    
    def display(self):
        print(f"Room Name: {self.name}")
        print(self.description)


class BattleRoom(Room):
    def __init__(self, name):
        super().__init__(
            name,
            room_type="battle",
            description="ENTERED: BATTLEROOM.",
        )
        self.battle_type = 'normal'
        self.enemy = None
        self.reward = None
        
    def display(self):
        super().display()
        print(f"Enemy: {self.enemy}")
        print(f"Battle Type: {self.battle_type}")
        print(f"Reward: {self.reward}")    
        

class BossRoom(Room):
    def __init__(self, name):
        super().__init__(
            name,
            room_type="boss",
            description="STAGE 3: FINALS \nWe have come to the final round of the tournament who will be crowned the champion \nYou are in the boss room. Defeat the boss to win the game!"
        )
        self.battle_type = 'normal'
        self.enemy = None
        self.reward = None


class EliteBattleRoom(Room):
    """Contains 2 elite enemies that have to be defeated to proceed."""
    def __init__(self, name):
        super().__init__(
            name,
            room_type="elite",
            description="STAGE 2: SEMI-FINALS\nCompetitors, welcome to the semi-finals of the tournament\nPlease proceed to choose your opponents"
        )
        self.battle_type = 'elite'
        self.enemy = None
        self.reward = None
        self.enemy2 = None
        self.reward2 = None
        
    def display(self):
        print(self.description)
        print(f"Battle Type: {self.battle_type}")
        print(f"Enemy 1: {self.enemy}")
        print(f"Reward 1: {self.reward}")
        print(f"Enemy 2: {self.enemy2}")
        print(f"Reward 2: {self.reward2}")


class TreasureRoom(Room):
    def __init__(self, name):
        super().__init__(
            name,
            room_type="treasure",
            description="You are in a treasure room.",
        )
        self.item = None
        
    def display(self):
        """displays the item assigned to the room"""
        super().display()
        print(f"Item: {self.item}")
