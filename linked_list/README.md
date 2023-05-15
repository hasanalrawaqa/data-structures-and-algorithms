# Challenge 06

Write the following methods for the Linked List class:

- append:

arguments: new value

adds a new node with the given value to the end of the list

- insert before

arguments: value, new value

adds a new node with the given new value immediately before the first node that has the value specified

- insert after

arguments: value, new value

adds a new node with the given new value immediately after the first node that has the value specified

## append method

<hr>

## Whiteboard Process

![Alt text](append%20whiteboard.PNG)

## Approach & Efficiency

Approach:
To append a value to the end of the linked list, we traverse the list until we reach the last node. Then, we update the next reference of the last node to point to the new node containing the appended value.

Efficiency:

Time complexity: O(n) in the worst case, where n is the number of nodes in the linked list. Since we need to traverse the entire list to reach the end, the time complexity is directly proportional to the size of the list.
Space complexity: O(1). The append operation only requires creating a new node, so the space complexity is constant.

## Solution

[link to code](linked_list/linked_list.py)

## insert before 

<hr>

## Whiteboard Process

![Alt text](insert%20before%20white%20board.PNG)

## Approach & Efficiency

Approach:
To insert a value before a target value in the linked list, we traverse the list until we find the target value or reach the end. Then, we insert the new node before the target value by updating the next references of the nodes accordingly.

Efficiency:

Time complexity: O(n) in the worst case, where n is the number of nodes in the linked list. If the target value is not found, we need to traverse the entire list. The time complexity is directly proportional to the size of the list.
Space complexity: O(1). The insert_before operation only requires creating a new node, so the space complexity is constant.

## Solution

[link to code](linked_list/linked_list.py)


## insert after

<hr>

## Whiteboard Process

![Alt text](insert%20after%20whiteboard.PNG)

## Approach & Efficiency

Approach:
To insert a value after a target value in the linked list, we traverse the list until we find the target value or reach the end. Then, we insert the new node after the target value by updating the next references of the nodes accordingly.

Efficiency:

Time complexity: O(n) in the worst case, where n is the number of nodes in the linked list. If the target value is not found, we need to traverse the entire list. The time complexity is directly proportional to the size of the list.
Space complexity: O(1). The insert_after operation only requires creating a new node, so the space complexity is constant.

## Solution

[link to code](linked_list/linked_list.py)