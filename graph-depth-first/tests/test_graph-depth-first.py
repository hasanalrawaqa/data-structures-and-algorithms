import pytest
from graph_depth_first import Node, Graph

@pytest.fixture
def sample_graph():
    graph = Graph()
    nodes = [Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('F'), Node('G'), Node('H')]
    graph.nodes = nodes

    # Create connections between nodes
    nodes[0].neighbors = [nodes[1], nodes[2]]
    nodes[1].neighbors = [nodes[3], nodes[4]]
    nodes[2].neighbors = [nodes[5], nodes[6]]
    nodes[4].neighbors = [nodes[7]]

    return graph, nodes

def test_depth_first(sample_graph):
    graph, nodes = sample_graph
    start_node = nodes[0]
    result = graph.depth_first(start_node)
    expected_result = ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
    assert result == expected_result

def test_depth_first_empty_graph():
    graph = Graph()
    start_node = Node('A')
    result = graph.depth_first(start_node)
    expected_result = ['A']  # Only the starting node
    assert result == expected_result

def test_depth_first_single_node(sample_graph):
    _, nodes = sample_graph
    start_node = nodes[4]  # Single node without neighbors
    result = start_node.depth_first(start_node)
    expected_result = ['E']  # Only the single node
    assert result == expected_result

if __name__ == "__main__":
    pytest.main()
