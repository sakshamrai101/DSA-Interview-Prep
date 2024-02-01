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
        queue = []
        results = []
        current_node = self.root
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results 
    

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results 



        


new_tree = BinarySearchTree()
new_tree.insert(47)
new_tree.insert(21)
new_tree.insert(76)
new_tree.insert(18)
new_tree.insert(27)
new_tree.insert(52)
new_tree.insert(82)

print(new_tree.BFS())
print(new_tree.dfs_pre_order())
print(new_tree.dfs_post_order())
print(new_tree.dfs_in_order())

