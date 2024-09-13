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



    def __r_contains(self, current_node, value):
        if current_node == None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value) 

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)  

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)

        if value == current_node.value:
            return False

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 

        return current_node
    

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.right is None and current_node.left is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left 
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
                
        return current_node
    

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)



        


new_tree = BinarySearchTree()
new_tree.insert(47)
new_tree.insert(21)
new_tree.insert(76)
new_tree.insert(18)
new_tree.insert(27)
new_tree.insert(52)
new_tree.insert(82)
new_tree.r_insert(65)

new_tree.delete_node(65)
print(new_tree.BFS())

