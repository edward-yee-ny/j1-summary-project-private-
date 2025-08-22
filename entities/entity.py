from objects.item import Item

class Entity:
    """An Entity class. Should have health, attack and some basic information."""
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
    
    def display_stats(self) -> None:
        print(f"""
HP: {self.hp}
ATK: {self.atk}
            \n""")
        return
    
    def update_hp(self, difference):
        """Updates HP of entity by difference. To damage, difference < 0."""
        self.hp += difference