from .room import Room, BattleRoom, TreasureRoom

from entities.enemy import Enemy

from objects.item import Item
from objects.item import WEAPON, ARMOR

from helper.shuffle_positions import shuffleListPositions

from helper import extractJson

_room_data = extractJson('data/rooms.json')
_item_data = extractJson('data/items.json')
_monster_data = extractJson('data/monsters.json')

def create_room(name: str) -> Room:
    data = _room_data[name]
    room_type = data["type"]
    description = data["description"]    
    if room_type == "battle":
        return BattleRoom(name, description)
    elif room_type == "treasure":
        return TreasureRoom(name, description)
    else:
        return Room(name, description)

class Map:
    def __init__(self):
        # saves the directions here
        self.direction_save_arr = []
        monsterData = {}
        itemsData = {}

        monsterData = extractJson('data/monsters.json')

        itemsData = extractJson('data/items.json')
        
        basicEnemiesRaw = monsterData['basic_enemies']
        eliteEnemiesRaw = monsterData['elite_enemies']
        
        basicEnemies = []
        eliteEnemies = []
        
        for enemy in basicEnemiesRaw:
            basicEnemies.append(Enemy(enemy['hp'], enemy['atk'], enemy['name'], 'basic'))
            
        for enemy in eliteEnemiesRaw:
            eliteEnemies.append(Enemy(enemy['hp'], enemy['atk'], enemy['name'], 'elite'))
        
        itemsDataRaw = itemsData['items']
        
        itemsData = []
        
        for item in itemsDataRaw:
            if item['type'] == WEAPON:
                itemsData.append(Item(0, item['atk'], item['name'], item['type']))
            else:
                itemsData.append(Item(item['hp'], 0, item['name'], item['type']))
        
        self.rooms: dict[str, Room] = {}
        for name in _room_data:
            room = create_room(name)
            self.rooms[name] = room

        basicEnemyIndexes = shuffleListPositions(list(range(len(basicEnemies))))
        eliteEnemyIndexes = shuffleListPositions(list(range(len(eliteEnemies))))
        itemIndexes = shuffleListPositions(list(range(len(itemsData))))

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
    
    
