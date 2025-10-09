ARMOR = 'armor'
WEAPON = 'weapon'


class Item:
    '''An item, possibly a reward or a treasure item.'''
    def __init__(self, name):
        self.name = name
        

class Weapon(Item):
    def __init__(self, name: str, atk: int):
        super().__init__(name)
        self.atk = atk


class Armor(Item):
    def __init__(self, name: str, hp: int):
        super().__init__(name)
        self.hp = hp
