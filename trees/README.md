# ***Code Challenge: Class 13***

## ***Task: Binary-Tree-max.***

## ***Whiteboard Process***

![whiteboard](whiteboard.png)

## ***Approach & Efficiency***

Approach:
The approach is to perform a depth-first search (DFS) traversal of the binary tree. We use a recursive helper function `_find_max` to traverse the tree and find the maximum value. At each node, we compare the node's value with the maximum values found in the left and right subtrees. We return the maximum value among these three options.

Efficiency:
The time complexity of this approach is O(N), where N is the number of nodes in the binary tree. This is because we need to visit every node in the tree to find the maximum value.

The space complexity is O(H), where H is the height of the binary tree. In the worst case, if the binary tree is skewed and resembles a linked list, the height can be equal to the number of nodes, resulting in O(N) space complexity. However, in a balanced binary tree, the height is approximately log(N), resulting in O(log(N)) space complexity.

Overall, the algorithm is efficient and can handle binary trees of varying shapes and sizes.

## ***Solution***

[link to code](binary_tree.py)
