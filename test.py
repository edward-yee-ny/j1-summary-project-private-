import unittest
from entities.player import Player
from entities.monster import Enemy

class TestEntities(unittest.TestCase):

    def test_player(self):
        player = Player(100, "John", "He is a guy")
        print(player.display_stats())
        self.assertIsInstance(player.calculate_atk(), int)
        
    def test_enemy(self):
        enemy = Enemy(100, 100, "Jack", "He is a horrible guy", "boss")
        print(enemy.enemy_type)
        

if __name__ == '__main__':
    unittest.main()