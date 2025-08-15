from random import random
from entities.entity import Entity
from objects.item import Item, ARMOR, WEAPON

class Player(Entity):
    """The Player character. Several methods to manipulate inventory and weapon."""
    def __init__(self, hp, name, description):
        super().__init__(hp, None, name, description)
        self.inventory = []
        self.cur_weapon = None
        self.cur_armor = None
    
    def open_inventory(self):
        """Prints out the current items stored in a player's inventory."""
        print("Your current items:", " ".join(self.inventory))
        return
    
    def update_inventory(self, item):
        """Updates the current inventory. RIGHT NOW, ONLY ADDS ITEM."""
        self.inventory.append(item)
        return
    
    def calculate_atk(self) -> int:
        """Calculates the attack that this Player should deal."""
        if not self.cur_weapon:
            return round((1+random()) * 100) # Fist? As if!!
        return round((1+random()) * self.cur_weapon.atk) # WEAPON ATTACK HERE
    
    def calculate_dmg(self, base_dmg):
        """Calculates total damage based on base damage and armor reduction."""
        self.hp -= base_dmg
        
        return
    
    def update_equipment(self, item: Item):
        """Updates the current weapon. ```type``` can either be player.ARMOR or player.WEAPON"""
        if item.type == ARMOR:
            self.cur_armor = item
        elif item.type == WEAPON:
            self.cur_weapon = item
        return