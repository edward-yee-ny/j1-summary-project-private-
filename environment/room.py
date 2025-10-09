"""Room types for the game environment."""


class Room:
    def __init__(self,
                 name: str,
                 description: str,
                 rooms: dict[str, str] | None = None):
        self.name = name
        self.description = description
        self._right: "Room | None" = None
        self._left: "Room | None" = None
        self._forward: "Room | None" = None
        self.visit_status = False
        self.isCompleted = False
        self.rooms: dict[str, str | None] = {
            "left": None,
            "forward": None,
            "right": None
        }
        if rooms:
            for direction, room_name in rooms.items():
                if direction not in self.rooms:
                    raise ValueError(f"Invalid direction: {direction!r}")
                self.rooms[direction] = room_name

    def get_forward(self) -> str | None:
        return self.rooms["forward"]

    def get_left(self) -> str | None:
        return self.rooms["left"]

    def get_right(self) -> str | None:
        return self.rooms["right"]

    def set_forward(self, room: str) -> None:
        self.rooms["forward"] = room

    def set_left(self, room: str) -> None:
        self.rooms["left"] = room

    def set_right(self, room: str) -> None:
        self.rooms["right"] = room

    def is_last_room(self) -> bool:
        return (
            self.get_left() is None and
            self.get_forward() is None and
            self.get_right() is None
        )

    def display(self) -> None:
        print(f"Room Name: {self.name}")
        print(self.description)


class BattleRoom(Room):
    """Contains one or more enemies that have to be defeated to proceed."""
    def __init__(self, name, description):
        super().__init__(name, description)
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


class TreasureRoom(Room):
    """Contains an item that can be picked up."""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.item = None

    def get_item(self):
        return self.item

    def set_item(self, item) -> None:
        self.item = item

    def display(self):
        """displays the item assigned to the room"""
        super().display()
        print(f"Item: {self.item}")
