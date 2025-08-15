from battle import BattleRoom
from boss import BossRoom
from room import Room
from treasure import TreasureRoom

class Map:
    def __init__(self):
        startRoom = Room()
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
        
        treasureRoom1.right = battleRoom2
        treasureRoom1.left = elitebattleRoom
        
        battleRoom2.forward = treasureRoom2
        
        treasureRoom2.left = elitebattleRoom
        treasureRoom2.right = treasureRoom3
        
        treasureRoom3.left = elitebattleRoom
        treasureRoom3.right = battleRoom3
        
        battleRoom3.forward = bossRoom
        
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
        
    def get_map(self):
        pass
    
if __name__ == "__main__":
    testMap = Map()
    testMap.head.display()
    testMap.go_right()
    testMap.go_forward()
    testMap.go_left()
    testMap.go_forward()
    testMap.go_right()
    testMap.go_forward()
    testMap.go_left()
    testMap.go_forward()
    testMap.go_right()