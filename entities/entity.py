from objects.item import Item

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