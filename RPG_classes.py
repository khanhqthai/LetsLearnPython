class Character:
    
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    
    def __init__(self, name, hp):
        super().__init__(name, hp, level)
    
    def speak(self):
        return "hey"
    
