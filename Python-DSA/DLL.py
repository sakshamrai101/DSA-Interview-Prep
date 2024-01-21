class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Constructor for Doubly-Linked List Class
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    # Add an element at the end of the list. 
    def append(self, value):
        new_node = Node(value)

        # Appending into empty list. 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True 
        
        # Adjusting tail pointer to add element. 
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True 
    

    # Remove items from the end of the list. 
    def pop_last(self):

        # If list is empty 
        if self.head is None:
            return False 

        res = self.tail
        # If list only contains one item. 
        if self.length == 1:
            self.head = None
            self.tail = None
        # List contains two or more items.
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            res.prev = None
        self.length -= 1
        return res
    
    def prepend(self, value):
        new_node = Node(value)

        # Prepending into empty list.
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # When list is not empty. 
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True  


    def pop_first(self):
        # Popping from the start in an empty list.
        if self.head is None:
            return None
        
        res = self.head
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:
            self.head = self.head.next
            self.head.prev = None 
            res.next = None 
        self.length -= 1
        return res
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        if self.head is None:
            return None 
        
        res = self.head 
        if index < self.length/2:
            for _ in range (index):
                res = res.next
        else:
            res = self.tail 
            for _ in range(self.length - 1, index, -1):
                res = res.prev
        return res  
    
    def set(self, index, value):
        res = self.get(index)
        if res:
            res.value = value
            return True
        return False 

    def insert(self, index, value):

        #Index out of bounds. 
        if index < 0 or index >= self.length:
            return False
        # Inserting at the start of the linked-list. 
        if index == 0:
            return self.prepend(value)
        # Inserting at the end of the linked list. 
        if index == self.length - 1:
            return self.append(value)
        
        # Creating new node and 2 variables to one after and one before the required index. 
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        # Insert the node in the list. 
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        #Index out of bounds. 
        if index < 0 or index >= self.length:
            return False
        # Removing from the start of the linked-list. 
        if index == 0:
            return self.pop_first()
        # Removing from the end of the linked list. 
        if index == self.length - 1:
            return self.pop_last()
        
        # De-linking previous and next node from current node. 
        res = self.get(index)
        res.next.prev = res.prev
        res.prev.next = res.next
        
        # De-linking current node from the list. 
        res.next = None
        res.prev = None 
        self.length -= 1
        return res

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.insert(1, 'zzz')
#my_doubly_linked_list.pop_last()
#my_doubly_linked_list.prepend(999)
#my_doubly_linked_list.pop_first()

my_doubly_linked_list.print_list()
print("Current Length of Doubly Linked List is: ", my_doubly_linked_list.length)
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()
