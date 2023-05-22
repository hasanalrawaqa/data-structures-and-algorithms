# Challenge 08

The challenge is to merge two linked lists, list1 and list2, by alternating their elements. The goal is to create a new merged linked list, new_list, where the elements from list1 and list2 are arranged in an alternating fashion.

## Whiteboard Process

![Alt text](zip_lists%20whiteboard.PNG)

## Approach & Efficiency

- ***Approach***:

The approach taken in the code is to use two pointers, current_node1 and current_node2, to iterate through list1 and list2 respectively. The algorithm iteratively alternates the next pointers of the nodes in list1 and list2 to achieve the desired merging. It also maintains a separate linked list, new_list, to store the merged elements.

 The algorithm starts by handling some base cases. If either list1 or list2 is empty, the non-empty list is returned as the merged list. Then, the algorithm initializes the pointers and a few temporary variables.

Next, it enters a while loop that continues until both current_node1 and current_node2 become None. Inside the loop, the algorithm performs the merging steps:

It stores the next nodes of current_node1 and current_node2 in temporary variables.
It updates the next pointers of current_node1 and current_node2 to alternate their positions.
It appends the values of current_node1 and current_node2 to the new_list.
It moves the pointers current_node1 and current_node2 to their respective next nodes using the temporary variables.
After the loop, the algorithm checks if there are any remaining nodes in either list1 or list2. If so, it appends the remaining nodes to new_list.

- ***Efficiency:***

The time complexity of the algorithm is O(max(N, M)), where N is the length of list1 and M is the length of list2. This is because the algorithm iterates through both linked lists in a single pass, considering the longer list. The operations performed in each iteration, such as updating next pointers and appending to new_list, take constant time.

The space complexity is also O(max(N, M)) because the algorithm creates a new linked list, new_list, to store the merged elements. The space required by new_list is proportional to the length of the longer input list.

## Solution

[link to code](linked_list/linked_list.py)
