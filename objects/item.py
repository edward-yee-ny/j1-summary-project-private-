ARMOR = 'armor'
WEAPON = 'weapon'

class Item:
    '''An item, possibly a reward or a treasure item.'''
    def __init__(self, hp, atk, name, type):
        self.hp = hp
        self.atk = atk
        self.name = name
        self.type = type
        
    def __repr__(self):
        return f"""{self.name} (TYPE: {self.type}, HP: {self.hp}, ATK: {self.atk})"""
        