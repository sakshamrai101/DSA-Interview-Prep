class Node:
    def __init__(self, value):
        self.value = value 
        self.right = None 
        self.left = None 

class BinarySearchTree:
    def __init__(self):
        # Initialising an empty tree. 
        self.root = None


    def insert(self, value):
        new_node = Node(value)

        # Inserting in empty tree. 
        if self.root is None:
            self.root = new_node
            return True 
        
        # Variable to traverse the tree. 
        temp = self.root 

        while True:
            # Duplicate node exists, insert fails!
            if new_node.value == temp.value:
                return False 
            # Go left.
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True 
                temp = temp.left
            # Go right.
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains (self, value):
        if self.root is None:
            return False 
        
        # Variable to traverse the tree. 
        temp = self.root

        while temp:
            if temp.value == value:
                return True 
            if temp.value > value:
                temp = temp.left
            else:
                temp = temp.right

        return False 
    

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        
        


new_tree = BinarySearchTree()
new_tree.insert(10)
new_tree.insert(5)
new_tree.insert(13)
new_tree.insert(3)
new_tree.insert(6)
new_tree.insert(11)
new_tree.insert(17)

print(new_tree.contains(5))

