class HashTable():
    def __init__(self, size) -> None:
        self.size=size
        self.arr=[[] for _ in range(size)]
        pass
    
    def printme(self):
        print(self.arr)
    
    def add(self, val):
        pass
    pass

hh=HashTable(10)
hh.printme()
