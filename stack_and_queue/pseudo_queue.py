from stack  import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        return self.stack1.pop()
    
    def to_string(self):
        elements = []
        while not self.stack1.is_empty():
            elements.append(str(self.stack1.pop()))

        return ' -> '.join(elements)

    
if __name__=='__main__':
    
    # Create a PseudoQueue object
    queue = PseudoQueue()

# Enqueue values: 10, 15, 20
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)

# Enqueue value: 5
    queue.enqueue(5)

# The internal state after enqueue operations
# [5]->[10]->[15]->[20]

# Dequeue operation
    value = queue.dequeue()
    print(value)  # Output: 10

# The internal state after dequeue operation
# [5]->[10]->[15]

# Dequeue operation
    value = queue.dequeue()
    print(value)  # Output: 15
