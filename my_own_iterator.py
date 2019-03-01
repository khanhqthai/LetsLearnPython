class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current+=1
            return num
        raise StopIteration
c = Counter(3,10)

for i in c:
    print(i)
        
        
    