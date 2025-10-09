import random
from typing import Any

from .. import item
from .room import Room, BattleRoom, TreasureRoom

from entities.enemy import Enemy

from helper.shuffle_positions import shuffleListPositions

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
        # saves the directions here
        self.direction_save_arr = []

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

        self.head = "Starting Room"
        self.currentRoom = self.head

    def get_room(self, name: str) -> Room:
        if not name in self.rooms:
            raise ValueError(f"Room {name!r} does not exist.")
        return self.rooms[name]
        
    def go_right(self):
        currentRoom = self.get_room(self.currentRoom)
        assert isinstance(currentRoom, Room)
        rightRoom = currentRoom.get_right()
        if rightRoom is None:
            print("No room lies to the right.")
        elif currentRoom.is_last_room():
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.get_room(rightRoom)
            self.direction_save_arr.append("right")
            currentRoom.display()
    
    def go_left(self):
        currentRoom = self.get_room(self.currentRoom)
        assert isinstance(currentRoom, Room)
        leftRoom = currentRoom.get_left()
        if leftRoom is None:
            print("No room lies to the left.")
        elif currentRoom.is_last_room():
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.get_room(leftRoom)
            self.direction_save_arr.append("left")
            currentRoom.display()
    
    def go_forward(self):
        currentRoom = self.get_room(self.currentRoom)
        assert isinstance(currentRoom, Room)
        forwardRoom = currentRoom.get_forward()
        if forwardRoom is None:
            print("No room lies forward.")
        elif currentRoom.is_last_room():
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.get_room(forwardRoom)
            self.direction_save_arr.append('forward')
            currentRoom.display()
        
    def displayCurrentRoom(self):
        currentRoom = self.get_room(self.currentRoom)
        currentRoom.display()
    
    
