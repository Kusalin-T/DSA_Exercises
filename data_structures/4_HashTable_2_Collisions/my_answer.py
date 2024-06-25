import string
with open("data_structures\\4_HashTable_2_Collisions\\Solution\\nyc_weather.csv", 'r') as f:
    next(f)
    datetemp=dict()
    temps=[]
    for line in f:
        splitstr = line.strip().split(',')
        key, val = splitstr[0], splitstr[1]
        datetemp[key] = int(val)
        temps.append(int(val))
    print(datetemp) 
    print(f'Avg Temp week: {sum(temps[:7])/7:.2f}')   
    print(f'Max temp: {max(temps)}')
    print(f'Jan 9: {datetemp['Jan 9']}')
    print(f'Jan 4: {datetemp['Jan 4']}')

with open("data_structures\\4_HashTable_2_Collisions\\Solution\\poem.txt", 'r') as f:
    txt=f.read()
    txt = str(txt.translate
    (str.maketrans('', '', string.punctuation)))
    counts=dict()
    for w in txt.split():
        if w in counts:
            counts[w]+=1
        else:
            counts[w]=1    
    for k in counts.keys():
        print(f'{k}: {counts[k]},')


#Hash Table Linear Probing
class HashLP():
    def __init__(self, size=10) -> None:
        self.size=size
        self.arr=[None for _ in range(size)]

    def get_hash(self, key):
        acc=0
        for c in key:    
            acc+=ord(c)
        return acc%self.size    
    
    def probe_range(self, index):
        return [*range(index, self.size)] + [*range(0, index)]
    
    def find_slot(self, key, index):
        for i in self.probe_range(index):
            if not self.arr[i]:
                return i
            if self.arr[i][0]==key:
                return i
        raise Exception('Memory full HashLP')    
    
    def set(self, key, val):
        h=self.get_hash(key)
        self.arr[self.find_slot(key, h)] = (key, val)

    def get(self, key):
        h=self.get_hash(key)
        for i in self.probe_range(h):
            if self.arr[i][0]==key:
                return self.arr[i][1]
        return None
    
    def remove(self, key):
        h=self.get_hash(key)
        for i in self.probe_range(h):
            if self.arr[i][0]==key:
                self.arr[i] = None
                return

hh=HashLP(10)
hh.set('a', 10)
hh.set('a', 20)
hh.set('k', 90)
print(hh.arr)
print(hh.get('k'))
hh.remove('k')
print(hh.arr)