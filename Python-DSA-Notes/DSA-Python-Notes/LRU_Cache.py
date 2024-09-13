class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # map key to the Node 

        # Left and Right pointers to keep track of LRU and MRU:
        self.left, self.right = Node(0,0), Node(0,0) # Initialised to 0. 

        # Initially they point to each other, so that we can insert an element in between them. 
        self.left.next, self.right.prev = self.right, self.left


    # Helper functions to update the LRU and MRU 
        
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    # remove node from list  
    def remove(self, node):
        # 1 -> 2 -> 3, lets say we need to remove the middle node, we reassign prev.next and next.prev to next and prev
        prev, nxt = node.prev, node.nxt
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 
        
        # Now since, we have gotten a node, it becomes the least recently used cache. 

    
    def put(self, key: int, value: int) -> None:
        # Key, value pair already exists, so first remove it then add it back.
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value) # Key value pair added to hashmap. 
        # Now insert the node into the DLL also
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the Hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]