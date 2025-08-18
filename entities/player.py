from random import random
from entities.entity import Entity
from objects.item import Item, ARMOR, WEAPON

class Player(Entity):
    """The Player character. Several methods to manipulate inventory and weapon."""
    def __init__(self, hp, name, description):
        super().__init__(hp, 100, name, description)
        self.inventory = []
        self.cur_weapon = None
        self.cur_armor = None
    
    def reset_hp(self):
        '''Use this function to reset the Player's HP before each battle.'''
        self.hp = 1750
        if self.cur_armor:
            self.hp += self.cur_armor.hp
        
        return
    
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
        # For now, just use update_hp()... maybe when the game is more complicated,
        # add something here :)
        return self.update_hp(-base_dmg)
    
    def update_equipment(self, item: Item):
        """Updates the equipment."""
        if item.type == ARMOR:
            self.cur_armor = item
        elif item.type == WEAPON:
            self.cur_weapon = item
        return