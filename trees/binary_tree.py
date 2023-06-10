class Node:
    """A node in a binary tree."""

    def __init__(self, value):
        """
        Initialize a new node.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """A binary tree data structure."""

    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def preorder(self, node, result):
        """
        Perform a preorder traversal of the binary tree.

        Args:
            node: The current node in the traversal.
            result: A list to store the values in the traversal order.

        Returns:
            A list containing the values in the preorder traversal order.
        """
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def inorder(self, node, result):
        """
        Perform an inorder traversal of the binary tree.

        Args:
            node: The current node in the traversal.
            result: A list to store the values in the traversal order.

        Returns:
            A list containing the values in the inorder traversal order.
        """
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
        return result

    def postorder(self, node, result):
        """
        Perform a postorder traversal of the binary tree.

        Args:
            node: The current node in the traversal.
            result: A list to store the values in the traversal order.

        Returns:
            A list containing the values in the postorder traversal order.
        """
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)
        return result


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root :
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if not node.left :
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if not node.right :
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        if not node :
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)

if __name__ == "__main__":
# Testing
    tree = BinarySearchTree()

    # Test adding nodes
    tree.add(4)
    tree.add(2)
    tree.add(6)
    tree.add(1)
    tree.add(3)
    tree.add(5)
    tree.add(7)

    # Test tree traversals
    preorder_traversal = tree.preorder(tree.root, [])
    inorder_traversal = tree.inorder(tree.root, [])
    postorder_traversal = tree.postorder(tree.root, [])

    print("Preorder result:", preorder_traversal)
    print("Inorder result:", inorder_traversal)
    print("Postorder result:", postorder_traversal)

    # Test contains method
    print("Contains 5:", tree.contains(5))  # True
    print("Contains 8:", tree.contains(8))  # False
