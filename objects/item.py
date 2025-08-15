class Item:
    def __init__(self, hp, atk, name):
        self.hp = hp
        self.atk = atk
        self.name = name
        
    def display_stats(self):
        print(f"""
Name: {self.name}

HP: {self.hp}
ATK: {self.atk}
""")
        return
    