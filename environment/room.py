class Room:
    def __init__(self, name):
        self.right = None
        self.left = None
        self.forward = None
        self.visit_status = False
        self.name = name
        self.description = "You are in a room."
        self.room_type = None
    
    def display(self):
        print(f"Room Name: {self.name}")
        print(self.description)