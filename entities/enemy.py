from entities.entity import Entity

class Enemy(Entity):
    """An Enemy class. Should be developed further."""
    def __init__(self, hp, atk, name, enemy_type):
        super().__init__(hp, atk)
        self.name = name
        self.enemy_type = enemy_type
    
    def display_stats(self):
        print("ENEMY STATS:\n------------", end='')
        super().display_stats()

    def __repr__(self):
        return f"{self.name} (TYPE: {self.enemy_type}, HP: {self.hp}, ATK: {self.atk})"