# overriding class methods

class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self,key):
        print(f"The thing you want  {self.key}, is not here brah")
    
    def __setitem__(self, key, value):
    
    
data = GrumpyDict({"first":"lakers", "car":"Jeep"})
print(data)

