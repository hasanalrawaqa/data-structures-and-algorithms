# Code Challenge no.38:graph depth first

**Author: Hasan Alrawaqa**

## Whiteboard

![Alt text](image.png)

## Approach & Efficiency

### Approach:

1. **Graph Representation:** Your graph is represented using an adjacency list, where each vertex is associated with a list of its neighboring vertices (edges).

2. **Vertex:** The `Vertex` class represents individual vertices. It stores the value of the vertex and provides a human-readable representation through the `__str__` method.

3. **Edge:** The `Edge` class represents edges between vertices. It holds the weight of the edge (if any) and the target vertex it's connected to.

4. **Graph:** The `Graph` class handles all graph operations. It maintains a private dictionary (`__adj_list`) to store vertices as keys and their corresponding edges as values.

5. **Adding Vertices:** The `add_vertex` method creates a new `Vertex` object and adds it to the `__adj_list` as a key with an empty list of edges.

6. **Adding Edges:** The `add_edge` method adds edges between vertices. It first checks if both vertices exist, then adds an `Edge` object with a weight to the adjacency list of both vertices.

7. **Getting Vertices:** The `get_vertices` method returns a list of all vertices by extracting the keys from the `__adj_list`.

8. **Getting Neighbors:** The `get_neighbors` method returns a list of edges (neighbors) connected to a given vertex. It retrieves the corresponding list of edges from the `__adj_list` for the provided vertex.

9. **Size:** The `size` method returns the number of vertices in the graph, which is equivalent to the length of the `__adj_list`.

### Efficiency:

- **Adding a Vertex:** Adding a vertex to the graph is an O(1) operation, as it involves inserting a new key-value pair into a dictionary.

- **Adding an Edge:** Adding an edge between two vertices is also an O(1) operation. It involves appending an `Edge` object to the list of edges associated with both vertices.

- **Getting Vertices:** Retrieving all vertices using the `get_vertices` method takes O(V) time, where V is the number of vertices in the graph. This is because it involves extracting all keys from the `__adj_list`.

- **Getting Neighbors:** Getting neighbors of a vertex through the `get_neighbors` method is O(1), as it involves directly accessing the list of edges associated with the given vertex.

- **Size:** The `size` method simply returns the length of the `__adj_list`, so it's an O(1) operation.
Sure, here's the approach and efficiency analysis for the depth-first pre-order traversal on a graph:

**Approach:**

1. Initialize a set to keep track of visited nodes.
2. Initialize an empty list to store the traversal order.
3. Define a recursive function `dfs(node)` that performs the depth-first pre-order traversal:
   - Mark the current node as visited by adding it to the visited set.
   - Append the value of the current node to the traversal order list.
   - Iterate through each neighbor of the current node:
     - If the neighbor has not been visited, recursively call `dfs(neighbor)`.

4. Call the `dfs(start_node)` function with the starting node of the traversal.

**Efficiency Analysis:**

- **Time Complexity:** O(V + E)
  - V: Number of vertices (nodes) in the graph.
  - E: Number of edges (connections) in the graph.
  
  In the worst case, every node and every edge will be traversed once. Each node is visited once in the `dfs` function, and each edge is traversed once while iterating through neighbors.

- **Space Complexity:** O(V)
  - V: Number of vertices (nodes) in the graph.

  The space complexity is primarily determined by the `visited` set used to keep track of visited nodes during traversal. In the worst case, all nodes can be stored in the `visited` set.

The depth-first pre-order traversal is efficient in terms of space complexity as it only requires memory for storing the visited set and the traversal order list. The time complexity is determined by the number of vertices and edges in the graph. Since each node and edge is visited at most once, the algorithm's time complexity is linear with respect to the input size (number of nodes and edges).

## Solution
[link to code](graph-depth-first.py)
