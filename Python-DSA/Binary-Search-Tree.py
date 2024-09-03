class Node:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Create a new node 
        new_node = Node(value)

        # Empty Tree 
        if self.root is None:
            self.root = new_node
            return True 

        # Create a dummy node for traversing the tree. 
        temp = self.root

        while True:
            # Duplicate insertion not allowed 
            if new_node.value == temp.value:
                return False
            
            # condition to go right
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True 
                
                temp = temp.right
            # condition to go left 
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                
                temp = temp.left

    def contains(self, value):
        # Empty tree
        if not self.root:
            return False 
        # Value found at the root:
        if self.root.value == value:
            return True 
        
        temp = self.root

        while True:

            if temp.value == value:
                return True 
            
            if value < temp.value:
                if temp.left:
                    temp = temp.left
                else:
                    return False 
            else:
                if temp.right:
                    temp = temp.right
                else:
                    return False 
        
        return False
    
    
        

        





my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(12)
my_tree.insert(7)
my_tree.insert(144)
my_tree.insert(5)
my_tree.insert(19)
print(my_tree.root.right.right.left.value)
print(my_tree.root.left.value)
print(my_tree.root.value)
print(my_tree.contains(100))