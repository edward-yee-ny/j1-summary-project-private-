import random
from typing import Any

from .. import item
from .room import Room, BattleRoom, TreasureRoom

from entities.enemy import Enemy

from helper import extractJson

_room_data = extractJson('data/rooms.json')
_item_data = extractJson('data/items.json')
_monster_data = extractJson('data/monsters.json')

def create_item(data: dict[str, Any]) -> item.Item:
    """Creates an item (Weapon or Armor) based on the provided data."""
    if data['type'] == item.WEAPON:
        return item.Weapon(name=data['name'], atk=data['atk'])
    elif data['type'] == item.ARMOR:
        return item.Armor(name=data['name'], hp=data['hp'])
    else:
        raise ValueError(f"Unknown item type: {data['type']}")

def create_monster(data: dict[str, Any]) -> Enemy:
    """Creates an Enemy based on the provided data."""
    return Enemy(
        hp=data['hp'],
        atk=data['atk'],
        name=data['name'],
        enemy_type=data['type']
    )

def create_room(name: str) -> Room:
    """Creates a Room (Room, BattleRoom, or TreasureRoom) based on the provided name."""
    data = _room_data[name]
    room_type = data["type"]
    description = data["description"]    
    if room_type == "battle":
        return BattleRoom(name, description)
    elif room_type == "treasure":
        return TreasureRoom(name, description)
    else:
        return Room(name, description)

def pop_random(items: list) -> Any:
    """Removes and returns a random item from the list."""
    if not items:
        raise ValueError("items is empty")
    index = random.randrange(len(items))
    return items.pop(index)


class Map:
    def __init__(self):
        self._direction_history = []
        self.currentRoom = "Starting Room"

    def get_room(self, name: str) -> Room:
        if not name in self.rooms:
            raise ValueError(f"Room {name!r} does not exist.")
        return self.rooms[name]
    
    def reset(self) -> None:
        items = [
            create_item(item) for item in _item_data['items']
        ]
        basicEnemies = [
            create_monster(enemy) for enemy in _monster_data['basic_enemies']
        ]
        eliteEnemies = [
            create_monster(enemy) for enemy in _monster_data['elite_enemies']
        ]
        
        self.rooms: dict[str, Room] = {}
        for name, data in _room_data.items():
            room = create_room(name)
            if isinstance(room, BattleRoom):
                room_type = data["type"]
                for _ in range(data["enemies"]):
                    if room_type in ("elite", "boss"):
                        enemy = pop_random(eliteEnemies)
                    else:
                        enemy = pop_random(basicEnemies)
                    room.add_enemy(enemy)
            if isinstance(room, TreasureRoom):
                for _ in range(data["rewards"]):
                    item = pop_random(items)
                    room.set_item(item)
            self.rooms[name] = room

        self.currentRoom = "Starting Room"

    def get_direction_history(self) -> list[str]:
        return self._direction_history.copy()

    def record_direction(self, direction: str) -> None:
        self._direction_history.append(direction)

    def go_direction(self, direction: str) -> None:
        currentRoom = self.get_room(self.currentRoom)
        if currentRoom.is_last_room():
            print("This is the last room in the game.")
            return
        elif direction == "left":
            nextRoom = currentRoom.get_left()
        elif direction == "right":
            nextRoom = currentRoom.get_right()
        elif direction == "forward":
            nextRoom = currentRoom.get_forward()
        else:
            raise ValueError(f"Unknown direction: {direction}")
        if nextRoom is None:
            if direction == "forward":
                print("No room lies ahead.")
            else:
                print(f"No room lies to the {direction}.")
            return
        self.currentRoom = nextRoom
        self.record_direction(direction)
        self.get_room(self.currentRoom).display()

    def go_right(self):
        self.go_direction("right")

    def go_left(self):
        self.go_direction("left")

    def go_forward(self):
        self.go_direction("forward")

    def displayCurrentRoom(self):
        currentRoom = self.get_room(self.currentRoom)
        currentRoom.display()
    
    
