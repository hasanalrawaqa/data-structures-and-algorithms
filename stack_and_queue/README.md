# ***Stack and Queue***

## ***Task: Implement a stack and queue data structure***

## ***Whiteboard Process***

Not required

## ***Approach & Efficiency***

### ***Queue***

***Time Complexity Analysis***

- `enqueue()` function: This function has a time complexity of O(1) as it adds a new node with the given value to the back of the queue.

- `dequeue()` function: This function has a time complexity of O(1) as it removes and returns the value of the node from the front of the queue.

- `peek()` function: This function has a time complexity of O(1) as it returns the value of the node located at the front of the queue without removing it.

- `is_empty()` function: This function has a time complexity of O(1) as it checks whether or not the queue is empty by comparing the front property to None.

***Space Complexity Analysis***

- The space complexity of the Queue class is O(n), where n is the number of elements in the queue. This is because each element in the queue is stored as a node in the linked list.

### ***Stack***

***Time Complexity Analysis***

- `push()` function: This function has a time complexity of O(1) as it adds a new node with the given value to the top of the stack.

- `pop()` function: This function has a time complexity of O(1) as it removes and returns the value of the node from the top of the stack.

- `peek()` function: This function has a time complexity of O(1) as it returns the value of the node located at the top of the stack without removing it.

- `is_empty()` function: This function has a time complexity of O(1) as it checks whether or not the stack is empty by comparing the top property to None.

***Space Complexity Analysis***

- The space complexity of the Stack class is O(n), where n is the number of elements in the stack. This is because each element in the stack is stored as a node in the linked list.

## ***Solution***

The ***Queue*** class uses a linked list as the underlying data storage mechanism. It provides methods to enqueue (add) elements to the back of the queue, dequeue (remove) elements from the front of the queue, peek at the element at the front of the queue without removing it, and check if the queue is empty.

The ***Stack*** class also uses a linked list as the underlying data storage mechanism. It provides methods to push (add) elements to the top of the stack, pop (remove) elements from the top of the stack, peek at the element at the top of the stack without removing it, and check if the stack is empty.

These implementations ensure the desired time and space complexities for the operations performed on the Stack and Queue data structures.


