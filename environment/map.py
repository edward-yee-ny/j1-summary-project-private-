from .room import Room, BattleRoom, TreasureRoom

from entities.enemy import Enemy

from objects.item import Item
from objects.item import WEAPON, ARMOR

from helper.shuffle_positions import shuffleListPositions

from helper.extract_json import extractJson

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

        startRoom = Room(
            name='Starting Room',
            room_type='start',
            description="You are in the starting room. Choose a direction to proceed."
        )
        battleRoom1 = BattleRoom('Battle Room 1')
        treasureRoom1 = TreasureRoom('Treasure Room 1')
        battleRoom2 = BattleRoom('Battle Room 2')
        treasureRoom2 = TreasureRoom('Treasure Room 2')
        treasureRoom3 = TreasureRoom('Treasure Room 3')
        elitebattleRoom = BattleRoom('Elite Battle Room')
        battleRoom3 = BattleRoom('Battle Room 3')
        bossRoom = BattleRoom('Boss Battle Room')

        basicEnemyIndexes = shuffleListPositions(list(range(len(basicEnemies))))
        eliteEnemyIndexes = shuffleListPositions(list(range(len(eliteEnemies))))
        itemIndexes = shuffleListPositions(list(range(len(itemsData))))

        startRoom.set_left(battleRoom1)
        startRoom.set_forward(treasureRoom1)
        startRoom.set_right(battleRoom2)

        battleRoom1.set_forward(treasureRoom1)
        battleRoom1.add_enemy(basicEnemies[basicEnemyIndexes[0]])
        battleRoom1.add_reward(itemsData[itemIndexes[0]])

        treasureRoom1.set_right(battleRoom2)
        treasureRoom1.set_left(elitebattleRoom)
        treasureRoom1.set_item(itemsData[itemIndexes[1]])

        battleRoom2.set_forward(treasureRoom2)
        battleRoom2.add_enemy(basicEnemies[basicEnemyIndexes[1]])
        battleRoom2.add_reward(itemsData[itemIndexes[2]])

        treasureRoom2.set_left(elitebattleRoom)
        treasureRoom2.set_right(treasureRoom3)
        treasureRoom2.set_item(itemsData[itemIndexes[3]])

        treasureRoom3.set_left(elitebattleRoom)
        treasureRoom3.set_right(battleRoom3)
        treasureRoom3.set_item(itemsData[itemIndexes[4]])

        battleRoom3.set_forward(bossRoom)
        battleRoom3.add_enemy(basicEnemies[basicEnemyIndexes[2]])
        battleRoom3.add_reward(itemsData[itemIndexes[-1]])

        elitebattleRoom.set_left(bossRoom)
        elitebattleRoom.set_right(battleRoom3)
        elitebattleRoom.add_enemy(eliteEnemies[eliteEnemyIndexes[0]])
        elitebattleRoom.add_enemy(eliteEnemies[eliteEnemyIndexes[1]])
        elitebattleRoom.add_reward(itemsData[itemIndexes[-2]])
        elitebattleRoom.add_reward(itemsData[itemIndexes[-3]])

        bossRoom.add_enemy(eliteEnemies[eliteEnemyIndexes[2]])
        bossRoom.add_reward(itemsData[itemIndexes[-4]])

        self.head = startRoom
        self.currentRoom = self.head
        
    def go_right(self):
        if self.currentRoom.get_right() is None:
            print("No room lies to the right.")
        elif self.currentRoom.get_left() is None and self.currentRoom.get_forward() is None and self.currentRoom.get_right() is None:
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.currentRoom.get_right()
            self.direction_save_arr.append("right")
            self.currentRoom.display()
    
    def go_left(self):
        if self.currentRoom.get_left() is None:
            print("No room lies to the left.")
        elif self.currentRoom.get_left() is None and self.currentRoom.get_forward() is None and self.currentRoom.get_right() is None:
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.currentRoom.get_left()
            self.direction_save_arr.append("left")
            self.currentRoom.display()
    
    def go_forward(self):
        if self.currentRoom.get_forward() is None:
            print("No room lies forward.")
        elif self.currentRoom.get_left() is None and self.currentRoom.get_forward() is None and self.currentRoom.get_right() is None:
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.currentRoom.get_forward()
            self.direction_save_arr.append('forward')
            self.currentRoom.display()
        
    def displayCurrentRoom(self):
        self.currentRoom.display()
    
    
