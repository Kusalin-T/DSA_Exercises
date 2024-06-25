class HashTable():
    # Solving collision by using linkedlist/dynamic array
    def __init__(self, size) -> None:
        self.size=size
        self.arr=[[] for _ in range(size)]
        pass
    
    def printme(self):
        print(self.arr)
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size
    
    def add(self, key, val):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if key==element[0]:
                self.arr[h][idx] = (key, val)
                return
        self.arr[h].append((key, val))    
    
    def get(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if key==element[0]:
                return element[1]
        return None
    
    def remove(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if key==element[0]:
                del self.arr[h][idx]

hh=HashTable(10)
hh.printme()
hh.add('hello', 30)
hh.add('hello', 40)
hh.add('heo', 70)
hh.printme()
print(hh.get('heo'))
hh.remove('heo')
hh.printme()