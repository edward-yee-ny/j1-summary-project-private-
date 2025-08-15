from .battle import BattleRoom
from .boss import BossRoom
from .room import Room
from .treasure import TreasureRoom

from helper.extract_json import extractJson

class Map:
    def __init__(self):

        monsterData = {}
        itemsData = {}

        with open('data/monsters.json', 'r') as f:
            monsterData = extractJson(f.read())
            
        with open('data/items.json', 'r') as f:
            itemsData = extractJson(f.read())
        
        basicEnemies = monsterData['basic_enemies']
        eliteEnemies = monsterData['elite_enemies']
        itemsData = itemsData['items']
        
        startRoom = Room()
        startRoom.description = "You are in the starting room. Choose a direction to proceed."
        
        battleRoom1 = BattleRoom()
        treasureRoom1 = TreasureRoom()
        battleRoom2 = BattleRoom()
        treasureRoom2 = TreasureRoom()
        treasureRoom3 = TreasureRoom()
        elitebattleRoom = BattleRoom()
        battleRoom3 = BattleRoom()
        bossRoom = BossRoom()
        
        startRoom.left = battleRoom1
        startRoom.middle = treasureRoom1
        startRoom.right = battleRoom2
        
        battleRoom1.forward = treasureRoom1
        battleRoom1.battle_type = 'basic'
        battleRoom1.enemy = basicEnemies[0]
        battleRoom1.reward = itemsData[0]
        
        treasureRoom1.right = battleRoom2
        treasureRoom1.left = elitebattleRoom
        treasureRoom1.item = itemsData[-1]
        
        battleRoom2.forward = treasureRoom2
        battleRoom2.battle_type = 'basic'
        battleRoom2.enemy = basicEnemies[1]
        battleRoom2.reward = itemsData[1]
        
        treasureRoom2.left = elitebattleRoom
        treasureRoom2.right = treasureRoom3
        treasureRoom2.item = itemsData[-2]
        
        treasureRoom3.left = elitebattleRoom
        treasureRoom3.right = battleRoom3
        treasureRoom3.item = itemsData[-3]
        
        battleRoom3.forward = bossRoom
        battleRoom3.battle_type = 'basic'
        battleRoom3.enemy = basicEnemies[2]
        battleRoom3.reward = itemsData[2]
        
        elitebattleRoom.left = bossRoom
        elitebattleRoom.right = battleRoom3
        
        self.head = startRoom
        
        self.currentRoom = self.head
        
    def go_right(self):
        if self.currentRoom.right is None:
            print("No room lies to the right.")
        else:
            self.currentRoom = self.currentRoom.right
            self.currentRoom.display()
    
    def go_left(self):
        if self.currentRoom.left is None:
            print("No room lies to the left.")
        else:
            self.currentRoom = self.currentRoom.left
            self.currentRoom.display()
    
    def go_forward(self):
        if self.currentRoom.forward is None:
            print("No room lies forward.")
        else:
            self.currentRoom = self.currentRoom.forward
            self.currentRoom.display()
        
    def displayCurrentRoom(self):
        self.currentRoom.display()
    
    