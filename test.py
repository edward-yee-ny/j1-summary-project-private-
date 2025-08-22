import unittest
from entities.player import Player, ARMOR, WEAPON
from entities.enemy import Enemy
from objects.item import Item
from environment.battle import BattleRoom
from environment.boss import BossRoom
from environment.elite_battle_room import EliteBattleRoom

class TestEntities(unittest.TestCase):

    def test_player(self):
        # basic initialisation
        player = Player()
        player.display_stats()

        #Check if damage is an integer
        self.assertIsInstance(player.calculate_atk(), int)

        #Checking if items are stored in inventory
        op_item = Item(-1,-1,"God itself", WEAPON)
        player.update_inventory(op_item)
        player.update_equipment(op_item) #note: always update inventory, but updating equipment is a choice
        print(player.inventory)
        self.assertNotEqual(player.inventory, [])
        
    def test_enemy(self):
        enemy = Enemy(100, 100, "Jack", "boss")
        print(enemy.enemy_type)
        enemy.update_hp(-10)
        enemy.display_stats()
    
class TestObjects(unittest.TestCase):

    def test_item(self):
        op_item = Item(-1,-1,"God itself", WEAPON)
        print(op_item)

class TestRooms(unittest.TestCase):

    def test_battle(self):
        enemy = Enemy(100, 100, "Jack", "boss")
        op_item = Item(-1,-1,"God itself",WEAPON)
        r = BattleRoom()
        r.enemy = enemy
        r.reward = op_item
        r.display()

    def test_boss(self):
        enemy = Enemy(100, 100, "Jack", "boss")
        op_item = Item(-1,-1,"God itself",WEAPON)
        r = BossRoom()
        r.enemy = enemy
        r.reward = op_item
        r.display()

    def test_elite(self):
        enemy = Enemy(100, 100, "Jack", "boss")
        enemy2 = Enemy(100, 100, "Joseph", "boss")
        op_item = Item(-1,-1,"God itself",WEAPON)
        r = EliteBattleRoom()
        r.enemy = enemy
        r.enemy2 = enemy2
        r.reward = op_item
        r.reward2 = op_item
        r.display()

if __name__ == '__main__':
    unittest.main()