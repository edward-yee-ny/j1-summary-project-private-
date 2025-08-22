from .battle import BattleRoom
from .boss import BossRoom
from .room import Room
from .treasure import TreasureRoom
from .elite_battle_room import EliteBattleRoom

from entities.enemy import Enemy

from objects.item import Item
from objects.item import WEAPON, ARMOR

from helper.shuffle_positions import shuffleListPositions

from helper.extract_json import extractJson

class Map:
    def __init__(self):

        monsterData = {}
        itemsData = {}

        with open('data/monsters.json', 'r') as f:
            monsterData = extractJson(f.read())
            
        with open('data/items.json', 'r') as f:
            itemsData = extractJson(f.read())
        
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
        
        startRoom = Room()
        startRoom.description = "You are in the starting room. Choose a direction to proceed."
        
        battleRoom1 = BattleRoom()
        treasureRoom1 = TreasureRoom()
        battleRoom2 = BattleRoom()
        treasureRoom2 = TreasureRoom()
        treasureRoom3 = TreasureRoom()
        elitebattleRoom = EliteBattleRoom()
        battleRoom3 = BattleRoom()
        bossRoom = BossRoom()
        
        basicEnemyIndexes = shuffleListPositions(list(range(len(basicEnemies))))
        eliteEnemyIndexes = shuffleListPositions(list(range(len(eliteEnemies))))
        itemIndexes = shuffleListPositions(list(range(len(itemsData))))
                
        startRoom.left = battleRoom1
        startRoom.middle = treasureRoom1
        startRoom.right = battleRoom2
        
        battleRoom1.forward = treasureRoom1
        battleRoom1.enemy = basicEnemies[basicEnemyIndexes[0]]
        battleRoom1.reward = itemsData[itemIndexes[0]]
        
        treasureRoom1.right = battleRoom2
        treasureRoom1.left = elitebattleRoom
        treasureRoom1.item = itemsData[itemIndexes[1]]
        
        battleRoom2.forward = treasureRoom2
        battleRoom2.enemy = basicEnemies[basicEnemyIndexes[1]]
        battleRoom2.reward = itemsData[itemIndexes[2]]
        
        treasureRoom2.left = elitebattleRoom
        treasureRoom2.right = treasureRoom3
        treasureRoom2.item = itemsData[itemIndexes[3]]
        
        treasureRoom3.left = elitebattleRoom
        treasureRoom3.right = battleRoom3
        treasureRoom3.item = itemsData[itemIndexes[4]]
        
        battleRoom3.forward = bossRoom
        battleRoom3.enemy = basicEnemies[2]
        battleRoom3.reward = itemsData[itemIndexes[-1]]
        
        elitebattleRoom.left = bossRoom
        elitebattleRoom.right = battleRoom3
        elitebattleRoom.enemy = eliteEnemies[eliteEnemyIndexes[0]]
        elitebattleRoom.enemy2 = eliteEnemies[eliteEnemyIndexes[1]]
        elitebattleRoom.reward = itemsData[itemIndexes[-2]]
        elitebattleRoom.reward2 = itemsData[itemIndexes[-3]]
        
        bossRoom.enemy = eliteEnemies[eliteEnemyIndexes[2]]
        bossRoom.reward = itemsData[itemIndexes[-4]]
        
        self.head = startRoom
        
        self.currentRoom = self.head
        
    def go_right(self):
        if self.currentRoom.right is None:
            print("No room lies to the right.")
        elif self.currentRoom.left is None and self.currentRoom.forward is None and self.currentRoom.right is None:
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.currentRoom.right
            self.currentRoom.display()
    
    def go_left(self):
        if self.currentRoom.left is None:
            print("No room lies to the left.")
        elif self.currentRoom.left is None and self.currentRoom.forward is None and self.currentRoom.right is None:
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.currentRoom.left
            self.currentRoom.display()
    
    def go_forward(self):
        if self.currentRoom.forward is None:
            print("No room lies forward.")
        elif self.currentRoom.left is None and self.currentRoom.forward is None and self.currentRoom.right is None:
            print("This is the last room in the game.")
        else:
            self.currentRoom = self.currentRoom.forward
            self.currentRoom.display()
        
    def displayCurrentRoom(self):
        self.currentRoom.display()
    
    
