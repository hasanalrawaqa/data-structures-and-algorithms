class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = new_node

    def dequeue(self):
        if not self.front:
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        if not self.front:
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None
