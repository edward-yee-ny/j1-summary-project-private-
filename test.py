import unittest
from entities.player import Player, ARMOR, WEAPON
from entities.monster import Enemy
from objects.item import Item

class TestEntities(unittest.TestCase):

    def test_player(self):
        # basic initialisation
        player = Player(100, "John", "He is a guy")
        player.display_stats()

        #Check if damage is an integer
        self.assertIsInstance(player.calculate_atk(), int)

        #Checking if items are stored in inventory
        player.update_inventory("item")
        player.update_equipment(ARMOR, "jokes") #note: always update inventory, but updating equipment is a choice
        print(player.inventory)
        self.assertNotEqual(player.inventory, [])
        
    def test_enemy(self):
        enemy = Enemy(100, 100, "Jack", "He is a horrible guy", "boss")
        print(enemy.enemy_type)
        enemy.update_hp(-10)
        enemy.display_stats()
    
class TestObjects(unittest.TestCase):

    def test_item(self):
        op_item = Item(-1,-1,"God itself")
        op_item.display_stats()

if __name__ == '__main__':
    unittest.main()