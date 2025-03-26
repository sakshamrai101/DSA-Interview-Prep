class MyHashMap:
    def __init__(self):
        self.map = [] # Empty list of key-value pairs. 

    def put(self, key: int, value: int) -> None:
        for pair in self.map:
            # The required key already exists in the map
            if pair[0] == key:
                pair[1] = value
                break
        # Key does not exist, just append the pair of key, value
        self.map.append([key, value])
    
    def get(self, key: int) -> int:
        for pair in self.map:
            if pair[0] == key:
                return pair[1]
        return -1

    
    def remove(self, key: int) -> None:
        for pair in self.map:
            if pair[0] == key:
                self.map.remove(pair)
        


myhash = MyHashMap()
myhash.put(1, 2)
myhash.put(2, 2)
myhash.put(3, 6)
myhash.put(4, 111)
myhash.put(5, 222)
print(myhash.get(1))
print(myhash.get(5))
print(myhash.get(2))
print(myhash.get(3))
myhash.remove(5)
print(myhash.get(5))