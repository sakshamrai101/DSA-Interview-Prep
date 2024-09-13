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
        return res
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None 

        res = self.head 
        for _ in range(index):
            res = res.next
        
        res.value = value 
        return res.value
    
    def insert(self, index, value):

        # Index out of bounds 
        if index < 0 or index > self.length:
            return False   

        # Insert at the beginning of the list.          
        if index == 0:
            return self.prepend(value)
        # Inserting at the at the list. 
        if index == self.length:
            return self.append_list(value)
        

        new_node = Node(value)
        
        
        # Inserting the node and adjusting the pointers. 
        temp = self.get(index - 1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        # Index out of bounds error.
        if index < 0 or index >= self.length:
            return False 
        
        # Removing from the end of the list.
        if index == self.length - 1:
            return self.pop_last()
        
        # Removing from the end of the list. 
        if index == 0:
            return self.pop_first()
        
        # Fetching and removing the node. 
        temp = self.get(index - 1)
        res = temp.next
        temp.next = res.next
        res.next = None
        self.length -= 1

        return res 
    
    def reverse_list(self):
        temp = self.head 
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# Leetcode Questions 
            
    # Find middle of the node without using length attribute. 
    def find_middle_node(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    # Determine if the given linked-list has cycle in it.
    def has_cycle(self):
        slow, fast = self.head, self.head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False 
    
    def find_kth_from_end(self, k):
        if k <= 0:
            return None
        slow, fast = self.head, self.head 

        for i in range(k):
            if not fast:
                return None
            fast = fast.next

        while fast:
            slow= slow.next
            fast = fast.next
        
        return slow 





        


        
        
        

# New instance of LinkedList created. 
my_linked_list = LinkedList(1)



my_linked_list.append_list(2)
my_linked_list.append_list(3)
my_linked_list.append_list(4)
my_linked_list.append_list(5)
#my_linked_list.remove(4)
#my_linked_list.insert(6, 9000)
#my_linked_list.insert(0, 85)



#my_linked_list.prepend(1)
#my_linked_list.set_value(10, 10)
#print("Popped Node", my_linked_list.pop_last())
#print("Popped Node", my_linked_list.pop_last())
#print("New node added to front:", my_linked_list.head.value)
#print("Popped Node from front:", my_linked_list.pop_first())

#print("Element at 0 index is: ", my_linked_list.get(0))

#my_linked_list.reverse_list()
my_linked_list.print_list()
print("Middle node is: ", my_linked_list.find_middle_node().value)
print("Kth node from last is: ", my_linked_list.find_kth_from_end(2).value)

print("Length of Linked-List:", my_linked_list.length)