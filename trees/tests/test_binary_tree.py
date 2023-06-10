from binary_tree import BinarySearchTree
import pytest


def test_instantiate_empty_tree():
    tree = BinarySearchTree()
    assert tree.root is None


def test_instantiate_tree_with_single_root():
    tree = BinarySearchTree()
    tree.add(5)
    assert tree.root.value == 5


def test_add_left_and_right_child_to_node():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7


def test_preorder_traversal():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    result = tree.preorder(tree.root, [])
    assert result == [5, 3, 2, 4, 7]


def test_inorder_traversal():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    result = tree.inorder(tree.root, [])
    assert result == [2, 3, 4, 5, 7]


def test_postorder_traversal():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    result = tree.postorder(tree.root, [])
    assert result == [2, 4, 3, 7, 5]


def test_contains_existing_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    assert tree.contains(3) is True


def test_contains_non_existing_value():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    assert tree.contains(6) is False
