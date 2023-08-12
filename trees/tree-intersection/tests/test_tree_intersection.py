# test_tree_intersection.py
import pytest
from tree_intersection import TreeNode, tree_intersection, BinaryTree

def test_tree_intersection():
    tree1 = TreeNode(100)
    tree1.left = TreeNode(160)
    tree1.right = TreeNode(200)
    tree1.left.left = TreeNode(125)
    tree1.left.right = TreeNode(175)
    tree2 = TreeNode(42)
    tree2.left = TreeNode(160)
    tree2.right = TreeNode(500)
    tree2.left.left = TreeNode(125)
    tree2.left.right = TreeNode(175)
    assert tree_intersection(tree1, tree2) == [160, 125, 175]

def test_tree_intersection2():
    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)
    tree1.right.right = TreeNode(3)
    tree2 = TreeNode(1)
    tree2.right = TreeNode(2)
    tree2.right.right = TreeNode(3)
    assert tree_intersection(tree1, tree2) == [1, 2, 3]

def test_tree_intersection3():
    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)
    tree1.right.right = TreeNode(3)
    tree2 = TreeNode(4)
    tree2.right = TreeNode(5)
    tree2.right.right = TreeNode(6)
    assert tree_intersection(tree1, tree2) == []

def test_tree_intersection_empty_trees():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    assert tree_intersection(tree1, tree2) == []
