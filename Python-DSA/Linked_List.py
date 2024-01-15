class Node:
    # Constructor for the node.
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Constructor for the linkedlist. 
    def __init__(self, value):
        # New instance of node created. 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    # Adding items at the end. 
    def append_list(self, value):
        new_node = Node(value)
        if self.head == None:
             self.head = new_node
             self.tail = new_node
        else: 
            # Updating tail pointer to point to new node. 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # Removing items from the last.
    def pop_last(self):
    
        # Empty Linked-List.
        if self.head is None:
            return None 

        # Two variables to iterate to the second last node. 
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    # Adding items at the start. 
    def prepend(self, value):
        new_node = Node(value)

        # Case when list is empty.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

   # Remove elements from the front.  
    def pop_first(self):
        # Empty List. 
        if self.head is None:
            return None
        res = self.head
        # Only 1 element in list. 
        if self.length == 1:
            self.tail = None
            self.head = None
            return res.value 
        
        self.head = self.head.next 
        self.length -= 1

        return res.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 

        res = self.head 
        for _ in range(index):
            res = res.next
        return res.value



# New instance of LinkedList created. 
my_linked_list = LinkedList(4)



my_linked_list.append_list(5)
my_linked_list.append_list(6)
my_linked_list.prepend(1)
#print("Popped Node", my_linked_list.pop_last())
#print("Popped Node", my_linked_list.pop_last())
#print("New node added to front:", my_linked_list.head.value)
#print("Popped Node from front:", my_linked_list.pop_first())

print("Element at 1st index is: ", my_linked_list.get(2))

my_linked_list.print_list()

print("Length of Linked-List:", my_linked_list.length)