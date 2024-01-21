# Building a stack utilising a linked-list. 
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value 

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        # Only one top pointer that keeps track of the top of the stack. 
        self.top = new_node 
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
           self.top = new_node
        else:
           new_node.next = self.top
           self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.top is None:
           return None
        
        res = self.top 
        self.top = self.top.next
        res.next = None
        self.height -= 1
        return res



my_stack = Stack(1)
my_stack.push('A')
my_stack.push('B')
#my_stack.pop()
print("Popped Element: ", my_stack.pop().value)
my_stack.print_stack()
print("Height of current stack is: ", my_stack.height)
        