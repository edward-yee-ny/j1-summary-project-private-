class Room:
    def __init__(self):
        self.right = None
        self.left = None
        self.forward = None
        self.visit_status = False
        self.description = "You are in a room."
    
    def display(self):
        print(self.description)