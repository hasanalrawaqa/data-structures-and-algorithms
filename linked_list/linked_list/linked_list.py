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

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def insert_before(self, target_value, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        print(f"Target value '{target_value}' not found in the linked list.")

    def insert_after(self, target_value, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node:
            if current_node.value == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        raise ValueError(f"Target value '{target_value}' not found in the linked list.")

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
print(my_list)  # "1 -> 2 -> 3 -> NULL"

# check if a value is in the list
print(my_list.includes(2))  # True
print(my_list.includes(4))  # False

# append a value
my_list.append(4)
print(my_list)  # "1 -> 2 -> 3 -> 4 -> NULL"

# insert before a value
my_list.insert_before(3, 2.5)
print(my_list)  # "1 -> 2 -> 2.5 -> 3 -> 4 -> NULL"

# insert after a value
my_list.insert_after(2.5, 2.7)
print(my_list)  # "1 -> 2 -> 2.5 -> 2.7 -> 3 -> 4 -> NULL"
