import pytest
from collections import deque
from ..graph import Graph

def test_add_vertex():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    assert vertex_a in graph.get_vertices()

def test_add_edge():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    graph.add_edge(vertex_a, vertex_b, weight=5)
    neighbors_a = graph.get_neighbors(vertex_a)
    assert neighbors_a[0].vertex == vertex_b
    assert neighbors_a[0].weight == 5

def test_get_all_vertices():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertices = graph.get_vertices()
    assert len(vertices) == 3
    assert vertex_a in vertices
    assert vertex_b in vertices
    assert vertex_c in vertices

def test_get_neighbors_with_weight():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    graph.add_edge(vertex_a, vertex_b, weight=5)
    neighbors_a = graph.get_neighbors(vertex_a)
    assert neighbors_a[0].vertex == vertex_b
    assert neighbors_a[0].weight == 5

def test_graph_size():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    assert graph.size() == 3

def test_single_vertex_edge():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    assert vertex_a in graph.get_vertices()
    neighbors_a = graph.get_neighbors(vertex_a)
    assert len(neighbors_a) == 0
