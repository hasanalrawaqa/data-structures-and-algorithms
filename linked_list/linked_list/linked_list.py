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

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

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

    def kthFromEnd(self, k):
        if k < 0:
            raise ValueError("k should be a positive integer.")

        if self.head is None:
            raise Exception("The linked list is empty.")

        slow = fast = self.head

        for _ in range(k):
            if fast is None:
                raise Exception("k is greater than the length of the linked list.")
            fast = fast.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next

        return slow.value

    
    def zip_lists(list1, list2):
        if not list1.head:
            return list2.head
        if not list2.head:
            return list1.head

        current_node1 = list1.head
        current_node2 = list2.head
        temp1 = None
        temp2 = None
        new_list = LinkedList()

        while current_node1 and current_node2:
            temp1 = current_node1.next
            temp2 = current_node2.next

            current_node1.next = current_node2
            current_node2.next = temp1
            new_list.append(current_node1.value)
            new_list.append(current_node2.value)

            current_node1 = temp1
            current_node2 = temp2

        if current_node1:
            new_list.append(current_node1.value)
            current_node1 = current_node1.next

        if current_node2:
            new_list.append(current_node2.value)
            current_node2 = current_node2.next

        return new_list


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

# create another linked list
list1 = LinkedList()
list2 = LinkedList()

# populate the linked lists
list1.insert(1)
list1.insert(3)
list1.insert(5)

list2.insert(2)
list2.insert(4)
list2.insert(6)

# zip the lists
result = LinkedList.zip_lists(list1, list2)
print(result.to_list())  # [5, 6, 3, 4, 1, 2]
