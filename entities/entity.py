import random

class Entity:
    """An Entity class. Should have health, attack and some basic information."""
    def __init__(self, hp, atk, name, description):
        self.hp = hp
        self.atk = atk
        self.name = name
        self.description = description
    
    def display_stats(self) -> None:
        print(f"""
Name: {self.name}
- {self.description}

HP: {self.hp}
ATK: {self.atk}""")
        return
    
    def update_hp(self, difference):
        """Updates HP of entity by difference. To damage, difference < 0."""
        self.hp += difference

class Player(Entity):
    """The Player character. Several methods to manipulate inventory and weapon."""
    def __init__(self, hp, atk, name, description):
        super().__init__(hp, atk, name, description)
        self.inventory = []
        self.cur_weapon = None
    
    def open_inventory(self):
        """Prints out the current items stored in a player's inventory."""
        print("Your current items:", " ".join(self.inventory))
        return
    
    def update_inventory(self, item):
        """Updates the current inventory. RIGHT NOW, ONLY ADDS ITEM."""
        self.inventory.append(item)
        return
    
    def calculate_atk(self):
        """Calculates the attack that this Player should deal."""
        base = random.randint(1, 6)
        return base + self.cur_weapon.attack # WEAPON ATTACK HERE
    
    def update_weapon(self, item):
        """Updates the current weapon."""
        self.cur_weapon = item
        return

class Enemy(Entity):
    """An Enemy class. Should be developed further."""
    def __init__(self, hp, atk, name, description, enemy_type, atk_type):
        super().__init__(hp, atk, name, description)
        self.enemy_type = enemy_type
        self.atk_type = atk_type
