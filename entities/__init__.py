import random

from item import Armor, Inventory, Item, Weapon


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

    def take_damage(self, damage: int) -> None:
        """Updates HP of entity by damage.
        
        Has no effect if damage is less than or equal to 0.
        """
        if damage > 0:
            self.hp -= damage


class Combatant(Entity):
    """An entity that can engage in combat.
    
    Has equippable slots for weapons and armor.
    """

    def __init__(self, name: str, hp: int, atk: int, crit_chance: float):
        super().__init__(hp, atk)
        self.name = name
        self.crit_chance = crit_chance
        self.cur_weapon = None
        self.cur_armor = None

    def equip(self, item: Item) -> None:
        """Equips an item to the combatant."""
        if isinstance(item, Weapon):
            self.cur_weapon = item
        elif isinstance(item, Armor):
            self.cur_armor = item

    def get_weapon(self) -> Weapon | None:
        """Returns the currently equipped weapon, or None if no weapon is
        equipped.
        """
        return self.cur_weapon

    def get_armor(self) -> Armor | None:
        """Returns the currently equipped armor, or None if no armor is
        equipped.
        """
        return self.cur_armor

    def take_damage(self, damage: int) -> None:
        """Armor takes damage first, then HP."""
        armor = self.get_armor()
        if armor:
            while damage > 0 and armor.hp > 0:
                damage -= 1
                armor.hp -= 1
        super().take_damage(damage)


class Enemy(Combatant):
    """An Enemy class. Should be developed further."""

    def __init__(self, name: str, hp: int, atk: int, enemy_type: str):
        super().__init__(name, hp, atk, crit_chance=0)
        self.name = name
        self.enemy_type = enemy_type
    
    def display_stats(self):
        print("----- ENEMY STATS:-----")
        super().display_stats()

    def __repr__(self):
        return f"{self.name} (TYPE: {self.enemy_type}, HP: {self.hp}, ATK: {self.atk})"


class Player(Combatant):
    """The Player character.
    
    A combatant with an inventory.
    """
    def __init__(self, name: str, hp: int, atk: int, crit_chance: float = 0.2):
        super().__init__(name, hp, atk, crit_chance)
        self.max_hp = hp
        self.inventory = Inventory()
    
    def display_stats(self):
        print("----- YOUR STATS:-----")
        super().display_stats()
        
    def restore(self) -> None:
        '''Use this function to restore the Player's armor and HP.'''
        self.hp = self.max_hp
        armor = self.get_armor()
        if armor:
            armor.restore()
    
    def display_inventory(self) -> None:
        """Prints out the current items stored in a player's inventory."""
        print("Your current items:", ", ".join(self.inventory))

    def update_inventory(self, item: Item) -> None:
        """Updates the current inventory. RIGHT NOW, ONLY ADDS ITEM."""
        self.inventory.add(item)

