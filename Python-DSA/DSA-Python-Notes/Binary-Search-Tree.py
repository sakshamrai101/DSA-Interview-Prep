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
    
    def bfs(self):
        queue = []
        result = []
        current_node = self.root
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return result 
    

    def dfs_pre_order(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return result 
    
    def dfs_post_order(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        
        traverse(self.root)
        return result
    
    def dfs_in_order(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result 


        





my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.bfs())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())