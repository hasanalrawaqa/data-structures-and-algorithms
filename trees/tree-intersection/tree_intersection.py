
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    def get_tree_values(node, values):
        if node is not None:
            values.add(node.val)
            get_tree_values(node.left, values)
            get_tree_values(node.right, values)

    values_set1 = set()
    values_set2 = set()

    get_tree_values(tree1, values_set1)
    get_tree_values(tree2, values_set2)

    common_values = values_set1.intersection(values_set2)
    return list(common_values)
