class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = []

    def depth_first(self, start_node):
        visited = set()
        traversal_order = []

        def dfs(node):
            nonlocal visited
            visited.add(node)
            traversal_order.append(node.value)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_node)
        return traversal_order
