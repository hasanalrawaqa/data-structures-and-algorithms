# ***Code Challenge: Class 13***

## ***Task: Binary-Search-Tree.***

## ***Whiteboard Process***

no whiteboard

## ***Approach & Efficiency***

1. Node class:
   - The `Node` class represents a node in a binary tree.
   - It has three properties: `value` to store the value of the node, `left` to reference the left child node, and `right` to reference the right child node.
   - The `__init__` method initializes a new node with the given value and sets the left and right child nodes to `None`.

2. BinaryTree class:
   - The `BinaryTree` class represents a binary tree data structure.
   - It has one property: `root` to reference the root node of the tree.
   - The `__init__` method initializes an empty binary tree by setting the root node to `None`.
   - The three traversal methods (`preorder`, `inorder`, and `postorder`) are implemented using recursive depth-first traversal algorithms.
   - Each traversal method takes a `node` parameter representing the current node in the traversal and a `result` list to store the values in the traversal order.
   - The methods perform the appropriate traversal by recursively visiting the left child, processing the current node, and then recursively visiting the right child.
   - The traversal order is determined by the placement of the processing step (before, between, or after visiting the child nodes).
   - The methods return the `result` list containing the values in the traversal order.

3. BinarySearchTree class:
   - The `BinarySearchTree` class is a subclass of the `BinaryTree` class and represents a binary search tree data structure.
   - It inherits the properties and methods of the `BinaryTree` class.
   - The `add` method adds a new node with the given value to the binary search tree in the correct location.
   - The method first checks if the tree is empty. If it is, the new node becomes the root. Otherwise, it calls the `_add_recursive` method to recursively find the correct location to add the node.
   - The `_add_recursive` method compares the value with the current node and recursively navigates to the left or right child until it finds an appropriate spot to add the new node.
   - The `contains` method checks if the binary search tree contains a node with the given value.
   - The method calls the `_contains_recursive` method to recursively search for the value in the tree.
   - The `_contains_recursive` method compares the value with the current node and recursively navigates to the left or right child until it finds the value or reaches a leaf node.

Approach Complexity:

- Adding a node to the binary search tree (`add` method): The complexity depends on the height of the tree. In the worst case, if the tree is unbalanced (skewed), the height can be O(n), where n is the number of nodes. However, in the average case, the height is usually log(n), resulting in an average complexity of O(log n) for adding a node.
- Searching for a value in the binary search tree (`contains` method): The complexity depends on the height of the tree. Similar to adding a node, the worst-case complexity is O(n) in an unbalanced tree, and the average-case complexity is O(log n) in a balanced tree.

Efficiency:

- The binary tree traversal methods (`preorder`, `inorder`, and `postorder`) visit each node once, resulting in a time complexity of O(n), where n is the number of nodes in the tree.
- The space complexity of the traversal methods is O(h), where h is the height of the tree. This is because the recursive calls consume space on the call stack. In the worst case, for a skewed tree, the height is O(n), resulting in

 a space complexity of O(n). In a balanced tree, the height is O(log n), resulting in a space complexity of O(log n).
- The `add` and `contains` methods have similar space complexity to the traversal methods, as they use recursive calls to navigate the tree. The worst-case space complexity is O(n) for a skewed tree and O(log n) for a balanced tree.

Overall, the implementation is efficient for most cases, especially when the binary search tree is balanced. However, for highly unbalanced trees, the efficiency of adding a node or searching for a value can degrade to O(n), which is less desirable. Balancing techniques, such as AVL trees or red-black trees, can be used to maintain a balanced tree structure and improve efficiency in such cases.

## ***Solution***

[link to code](binary_tree.py)
