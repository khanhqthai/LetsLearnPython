class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age  = age
    
    def __repr__(self):
        return f"{self.first} {self.last}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, human):
        return Human(self, human.first, 0)
    
    def __mul__(self, num):
        return [self for i in range(num)]
    
    
nicole = Human("nicole", "B", 36)
mar = Human("mar", "L", 25)
baby = nicole + mar
print(len(baby))

print(nicole * 2)
    
        
