class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        values.append("NULL")
        return " -> ".join(values)

# create a new linked list
my_list = LinkedList()

# insert some values
my_list.insert(3)
my_list.insert(2)
my_list.insert(1)

# print the list
print(my_list) # "1 -> 2 -> 3 -> NULL"

# check if a value is in the list
print(my_list.includes(2)) # True
print(my_list.includes(4)) # False
