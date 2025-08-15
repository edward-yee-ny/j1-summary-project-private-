ARMOR = 'armor'
WEAPON = 'weapon'

class Item:
    '''An item, possibly a reward or a treasure item.'''
    def __init__(self, hp, atk, name, type):
        self.hp = hp
        self.atk = atk
        self.name = name
        self.type = type
        
    def display_stats(self):
        print(f"""
Name: {self.name} ({self.type})

HP: {self.hp}
ATK: {self.atk}
""")
        return