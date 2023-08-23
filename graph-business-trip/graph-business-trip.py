class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest, cost):
        if src not in self.graph:
            self.graph[src] = []
        self.graph[src].append((dest, cost))

    def get_neighbors(self, node):
        return self.graph.get(node, [])

def business_trip(graph, cities):
    if not graph or not cities:
        return None
    
    total_cost = 0

    for i in range(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        neighbors = graph.get_neighbors(current_city)
        found = False

        for neighbor, cost in neighbors:
            if neighbor == next_city:
                total_cost += cost
                found = True
                break

        if not found:
            return None

    return total_cost

# Create the graph and add routes
route_map = Graph()
route_map.add_edge('Metroville', 'Pandora', 82)
route_map.add_edge('Arendelle', 'New Monstropolis', 45)
route_map.add_edge('New Monstropolis', 'Naboo', 70)
# Add more edges as needed

# Test cases
print(business_trip(route_map, ['Metroville', 'Pandora']))  # Output: 82
print(business_trip(route_map, ['Arendelle', 'New Monstropolis', 'Naboo']))  # Output: 115
print(business_trip(route_map, ['Naboo', 'Pandora']))  # Output: None
print(business_trip(route_map, ['Narnia', 'Arendelle', 'Naboo']))  # Output: None
