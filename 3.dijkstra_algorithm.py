"""
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph. 
It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

The algorithm exists in many variants; Dijkstra's original variant found the shortest path 
between two nodes, but a more common variant fixes a single node as the "source" node and finds 
shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

For a given source vertex (node) in the graph, the algorithm finds the shortest path between 
that vertex and every other vertex. It can also be used for finding the shortest path from a 
single vertex to a single destination vertex by stopping the algorithm once the shortest path to 
the destination vertex has been determined.

The algorithm is implemented using a priority queue data structure to store the vertices 
and their distances.
The priority queue is implemented using a min heap, which allows for efficient retrieval 
of the vertex with the smallest distance.

Time complexity:
- __init__: O(V)
- add_edge: O(1)
- dijkstra: O(E * log V)
"""
import heapq

class Graph:
    """
    Class for representing a graph using adjacency list

    Attributes:
    - V: int - number of vertices in the graph
    - graph: dict - dictionary to store the graph

    Methods:
    - add_edge(u, v, weight): add an edge between vertices u and v with weight
    - dijkstra(src): find the shortest path from source vertex src to all other vertices

    Time complexity:
    - __init__: O(V)
    - add_edge: O(1)
    - dijkstra: O(E * log V)
    """
    def __init__(self, vertices):
        """
        Initialize the graph with the number of vertices.

        :param vertices: int - number of vertices in the graph

        :return: None

        Time complexity: O(V)
        """
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        """
        Add an edge between vertices u and v with weight.

        :param u: int - source vertex
        :param v: int - destination vertex
        :param weight: int - weight of the edge

        :return: None

        Time complexity: O(1)
        """
        self.graph[u].append((v, weight))

    def dijkstra(self, src):
        """
        Find the shortest path from source vertex src to all other vertices.

        :param src: int - source vertex

        :return: list - list of shortest distances from src to all other vertices

        Time complexity: O(E * log V)
        """
        
        # Initialize the distance array with infinity
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Min heap to store the vertices
        min_heap = []
        heapq.heappush(min_heap, (0, src)) # (distance, vertex)

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            # If the current distance is greater than the distance in the array, skip
            if current_dist > dist[u]:
                continue

            # Traverse through the adjacent vertices
            for v, weight in self.graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))

        return dist

if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    dist = g.dijkstra(0)
    print("Відстані від вершини 0 до всіх інших:")
    for index, distance in enumerate(dist):
        print(f"{index}: {distance}")
