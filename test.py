import unittest
from entities.entity import Player, Enemy

class TestEntities(unittest.TestCase):

    def test_player(self):
        player = Player(100, 100, "John", "He is a guy")
        #self.assertIsInstance(player.calculate_atk(), int)
        print(player.display_stats())
        
    def test_enemy(self):
        enemy = Enemy(100, 100, "Jack", "He is a horrible guy", "boss", "roar")
        print(enemy.enemy_type, enemy.atk_type)
        

if __name__ == '__main__':
    unittest.main()