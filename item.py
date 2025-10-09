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


class Inventory:
    def __init__(self):
        self._contents: dict[str, Item] = {}

    def __iter__(self) -> Iterator:
        return iter(self._contents)

    def add(self, item: Item) -> bool:
        """Add an item to inventory.

        Returns a bool representing success or failure.
        """
        if self.has(item.name):
            return False
        self._contents[item.name] = item
        return True

    def has(self, item_name: str) -> bool:
        """Returns True if the item is in inventory."""
        return item_name in self._contents

    def items(self) -> list[tuple[str, Item]]:
        return list(self._contents.items())

    def keys(self) -> list[str]:
        return list(self._contents.keys())

    def remove(self, item_name: str) -> bool:
        """Remove an item from inventory. 

        Returns a bool representing success or failure. 
        """
        if not self.has(item_name):
            return False
        del self._contents[item_name]
        return True

