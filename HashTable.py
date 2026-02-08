class HashTable:

    # constructor sets lists in keyMap
    def __init__(self, size):
        self.keyMap = [] # instance aot class variable
        for _ in range(size):
            self.keyMap.append(list())
    
    # to string method for class
    def __str__(self):
        return str(self.keyMap)
    
    # hash method
    def _hash(self, key):

        if key is None:
            return
        
        total = 0
        PRIME = 31
        key = str(key)
        
        for i in range(min(len(key), 100)):
            ch = key[i]
            value = ord(ch)
            total = (total * PRIME + value) % len(self.keyMap)

        return total

    # Set method
    def set(self, key, value):
        
        if key is None:
            return
        
        key = str(key)
        hashIndex = self._hash(key)
        bucket = self.keyMap[hashIndex]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value))

    # Get method
    def get(self, key):
        
        if key is None:
            return None
        
        key = str(key)
        hashIndex = self._hash(key)
        bucket = self.keyMap[hashIndex]

        for k, v in bucket:
            if k == key:
                return v
            
    # Keys method
    def keys(self):
        returnlist = []
        for l in self.keyMap:
            for k, v in l:
                returnlist.append(k)
        return returnlist

    # Values method
    def values(self):
        returnlist = []
        for l in self.keyMap:
            for k, v in l:
                returnlist.append(v)
        return returnlist
    
ht = HashTable(10)
ht.set("hello", "world")
ht.set("how", "are you")
print(ht.get("hello"))
print(ht.keys())
print(ht.values())
print(ht)