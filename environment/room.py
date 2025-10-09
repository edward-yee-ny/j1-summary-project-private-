"""Room types for the game environment."""


class Room:
    def __init__(self,
                 name: str,
                 room_type: str,
                 description: str):
        self.name = name
        self.description = description
        self.room_type = room_type
        self._right = None
        self._left = None
        self._forward = None
        self.visit_status = False
        self.isCompleted = False

    def get_forward(self) -> "Room":
        return self._forward

    def get_left(self) -> "Room":
        return self._left

    def get_right(self) -> "Room":
        return self._right

    def set_forward(self, room: "Room") -> None:
        self._forward = room

    def set_left(self, room: "Room") -> None:
        self._left = room

    def set_right(self, room: "Room") -> None:
        self._right = room

    def display(self) -> None:
        print(f"Room Name: {self.name}")
        print(self.description)


class BattleRoom(Room):
    """Contains one or more enemies that have to be defeated to proceed."""
    def __init__(self, name):
        super().__init__(
            name,
            room_type="battle",
            description="ENTERED: BATTLEROOM.",
        )
        self.enemies: list = []
        self.rewards: list = []

    def add_enemy(self, enemy) -> None:
        self.enemies.append(enemy)

    def add_reward(self, reward) -> None:
        self.rewards.append(reward)

    def display(self) -> None:
        super().display()
        if self.enemies:
            print(f"Enemies: {", ".join(str(enemy) for enemy in self.enemies)}")
        else:
            print("Enemies: None")
        if self.rewards:
            print(f"Rewards: {", ".join(str(reward) for reward in self.rewards)}")
        else:
            print("Rewards: None")


class BossRoom(Room):
    def __init__(self, name):
        super().__init__(
            name,
            room_type="boss",
            description="STAGE 3: FINALS \nWe have come to the final round of the tournament who will be crowned the champion \nYou are in the boss room. Defeat the boss to win the game!"
        )
        self.enemies: list = []
        self.rewards: list = []


class EliteBattleRoom(Room):
    """Contains 2 elite enemies that have to be defeated to proceed."""
    def __init__(self, name):
        super().__init__(
            name,
            room_type="elite",
            description="STAGE 2: SEMI-FINALS\nCompetitors, welcome to the semi-finals of the tournament\nPlease proceed to choose your opponents"
        )
        self.enemies: list = []
        self.rewards: list = []
        
    def display(self):
        print(self.description)
        print(f"Enemy 1: {self.enemy}")
        print(f"Reward 1: {self.reward}")
        print(f"Enemy 2: {self.enemy2}")
        print(f"Reward 2: {self.reward2}")


class TreasureRoom(Room):
    """Contains an item that can be picked up."""
    def __init__(self, name):
        super().__init__(
            name,
            room_type="treasure",
            description="You are in a treasure room.",
        )
        self.item = None

    def get_item(self):
        return self.item

    def set_item(self, item) -> None:
        self.item = item

    def display(self):
        """displays the item assigned to the room"""
        super().display()
        print(f"Item: {self.item}")
