import random

from item import Inventory, Item


class Entity:
    """An Entity class."""
    def __init__(self, hp: int, atk: int):
        self.hp = hp
        self.atk = atk
    
    def display_stats(self) -> None:
        print(f"""HP: {self.hp} ATK: {self.atk}""")

    def is_dead(self) -> bool:
        """Returns True if entity is dead, False otherwise."""
        return self.hp <= 0
    
    def update_hp(self, difference):
        """Updates HP of entity by difference. To damage, difference < 0."""
        self.hp += difference


class Enemy(Entity):
    """An Enemy class. Should be developed further."""
    def __init__(self, hp: int, atk: int, name: str, enemy_type: str):
        super().__init__(hp, atk)
        self.name = name
        self.enemy_type = enemy_type
    
    def display_stats(self):
        print("----- ENEMY STATS:-----")
        super().display_stats()

    def __repr__(self):
        return f"{self.name} (TYPE: {self.enemy_type}, HP: {self.hp}, ATK: {self.atk})"


class Player(Entity):
    """The Player character. Several methods to manipulate inventory and weapon."""
    def __init__(self, hp: int, atk: int):
        super().__init__(hp, atk)
        self.inventory = Inventory()
        self.cur_weapon = None
        self.cur_armor = None
    
    def display_stats(self):
        print("----- YOUR STATS:-----")
        super().display_stats()
        
    def reset_hp(self):
        '''Use this function to reset the Player's HP before each battle.'''
        self.hp = 1750
        if self.cur_armor:
            self.hp += self.cur_armor.hp
        
        return
    
    def display_inventory(self):
        """Prints out the current items stored in a player's inventory."""
        print("Your current items:", ", ".join(self.inventory))
        return
    
    def update_inventory(self, item: Item):
        """Updates the current inventory. RIGHT NOW, ONLY ADDS ITEM."""
        self.inventory.add(item)
        return
    
    def update_equipment(self, item: Item):
        """Updates the equipment."""
        if item.type == ARMOR:
            self.cur_armor = item
        elif item.type == WEAPON:
            self.cur_weapon = item
            self.atk = 200 + self.cur_weapon.atk
