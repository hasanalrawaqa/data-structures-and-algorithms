class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if not self.top:
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None
        