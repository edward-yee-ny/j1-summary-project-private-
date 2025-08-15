from entities.entity import Entity

class Enemy(Entity):
    """An Enemy class. Should be developed further."""
    def __init__(self, hp, atk, name, description, enemy_type, atk_type):
        super().__init__(hp, atk, name, description)
        self.enemy_type = enemy_type
        self.atk_type = atk_type
