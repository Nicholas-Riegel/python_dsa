from collections import namedtuple
from PriorityQueue import PriorityQueue

# create a named tuple (access: x.vertex, x.distance), immutable
# used in add_update_method_edge
Edge = namedtuple('Edge', ['vertex', 'distance'])

class WeightedGraph:

    # constructor
    # creates the dictionary
    def __init__(self):
        self.mainDictOfLists = {}

    # to string method
    # returns the stringified dictionary
    def __str__(self):
        lines = []
        for vertex, edges in self.mainDictOfLists.items():
            edge_strings = [f"{e.vertex}({e.distance})" for e in edges]
            lines.append(f"{vertex}: {', '.join(edge_strings)}")
        return '\n'.join(lines)
    
    # add vertex method
    def add_vertex(self, vertex):
        if vertex not in self.mainDictOfLists:
            self.mainDictOfLists[vertex] = []

    # add edge method
    def add_update_edge(self, v1, v2, distance):
        
        # make sure both vertices exist
        if v1 not in self.mainDictOfLists:
            self.add_vertex(v1)
        if v2 not in self.mainDictOfLists:
            self.add_vertex(v2)

        # helper function to remove duplicate before adding
        def find_remove_add(keyVertex, edge):
            # find a remove duplicate
            for v in self.mainDictOfLists[keyVertex]:
                if v.vertex == edge.vertex:
                    self.mainDictOfLists[keyVertex].remove(v)
            # add new edge
            self.mainDictOfLists[keyVertex].append(edge)
        
        find_remove_add(v1, Edge(v2, distance))
        find_remove_add(v2, Edge(v1, distance))
    
    # digkstra's algorithm 
    # for finding shortest path from start to end vertex
    # pseudocode:
    # 1. This function should accept a starting and ending vertex
    # 2. Create an object (we'll call it distances) and set each key to be every vertex in the adjacency list with a value of infinity, except for the starting vertex which should have a value of 0.
    # 3. Add each vertex to the priority queue: the starting vertex with a priority of 0, and all other vertices with a priority of infinity
    # 4. Create another object called previous and set each key to be every vertex in the adjacency list with a value of null
    # 5. Start looping as long as there is anything in the priority queue
    #     dequeue a vertex from the priority queue
    #     If that vertex is the same as the ending vertex - we are done!
    #     Otherwise loop through each value in the adjacency list at that vertex
    #         Calculate the distance to that vertex from the starting vertex
    #         if the distance is less than what is currently stored in our distances object
    #             update the distances object with new lower distance
    #             update the previous object to contain that vertex
    #             enqueue the vertex with the total distance from the start node
    def dijkstra(self, start, end):

        shortestDistancesFromStart = {} 
        previous = {}
        pq = PriorityQueue()

        for vertex in self.mainDictOfLists.keys():
            if vertex == start:
                shortestDistancesFromStart[vertex] = 0
                pq.enqueue(vertex, 0)
            else:
                shortestDistancesFromStart[vertex] = float('inf')
                pq.enqueue(vertex, float('inf'))
            previous[vertex] = None
        
        while pq:
            item = pq.dequeue()
            if item['vertex'] == end:
                return shortestDistancesFromStart[end]
            else:
                for neighbor in self.mainDictOfLists[item['vertex']]:

                    distanceFromVertexToStart = shortestDistancesFromStart[item['vertex']] + neighbor.distance
                    
                    if distanceFromVertexToStart < shortestDistancesFromStart[neighbor.vertex]:
                    
                        shortestDistancesFromStart[neighbor.vertex] = distanceFromVertexToStart
                    
                        previous[neighbor.vertex] = item['vertex']
                    
                        pq.enqueue(neighbor.vertex, distanceFromVertexToStart)




# testing
g = WeightedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_update_edge("A", "B", 4)
g.add_update_edge("A", "C", 2)
g.add_update_edge("B", "E", 3)
g.add_update_edge("C", "D", 2)
g.add_update_edge("C", "F", 4)
g.add_update_edge("D", "E", 3)
g.add_update_edge("B", "F", 1)
g.add_update_edge("E", "F", 1)

print(g)
print(g.dijkstra('A', 'E'))