# Challenge linked list

## Challenge Description

--------------------------------
A linked list is a linear data structure where each element is a separate object (node) consisting of a value and a reference to the next node.

This challenge is to implement a linked list class that has the following methods:

1. **insert**: which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
2. **includes**: which takes any value as an argument and returns a boolean result depending on whether that value exists as a node's value somewhere within the list.
3. **to_string**: which takes no arguments and returns a string representing all the values in the Linked List.

## Approach & Efficiency

----------------
For **insert** method, we will simply create a new node with the given value and make it the new head of the linked list. This has a time complexity of O(1).

For **includes** method, we will traverse the linked list and compare the value of each node to the given value until we find a match or reach the end of the list. This has a time complexity of O(n).

For **to_string** method, we will traverse the linked list and concatenate the string representation of each node's value into a single string separated by a " -> " delimiter. This also has a time complexity of O(n).

## Solution

 [link to code](linked_list.py)
