class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, value):
        self.vertices[value] = []
        
    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise ValueError("Both vertices should already be in the Graph")
        
        self.vertices[vertex1].append((vertex2, weight))
        self.vertices[vertex2].append((vertex1, weight))
        
    def get_vertices(self):
        return list(self.vertices.keys())
        
    def get_neighbors(self, vertex):
        if vertex not in self.vertices:
            return []
        return self.vertices[vertex]
        
    def size(self):
        return len(self.vertices)
from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)

class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

class Graph:
    def __init__(self):
        self.__adj_list = {}
      
    def add_vertex(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)

    def get_vertices(self):
        return list(self.__adj_list.keys())

    def size(self):
        return len(self.__adj_list)
  
    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])
