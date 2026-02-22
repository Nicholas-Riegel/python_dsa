from PriorityQueue import PriorityQueue

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
            edge_strings = [f"{e['vertex']}({e['distance']})" for e in edges]
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
                if v['vertex'] == edge['vertex']:
                    self.mainDictOfLists[keyVertex].remove(v)
            # add new edge
            self.mainDictOfLists[keyVertex].append(edge)
        
        find_remove_add(v1, {'vertex': v2, 'distance': distance})
        find_remove_add(v2, {'vertex': v1, 'distance': distance})
    
    # digkstra's algorithm 
    def dijkstra(self, start, end):

        # dict tracks shortest distance to start
        distances = {} 
        # dicts tracks previous vertex of shortest path to start
        previous = {}
        # pq always pick vertex with shortest distance
        priorityQ = PriorityQueue()

        for vertex in self.mainDictOfLists.keys():

            # set dict to track previous of shortest path            
            previous[vertex] = None
            
            if vertex == start:
                # set start distance to 0
                distances[vertex] = 0
                # add start with 0 distance to pq
                priorityQ.enqueue(vertex, 0)
            else:
                # set non-start vertices to inf
                distances[vertex] = float('inf')
                # load non-start vertices to pq
                priorityQ.enqueue(vertex, float('inf'))
        
        while True:

            # get current vertex
            item = priorityQ.dequeue()
            current_vertex = item['vertex']

            # if current vertex = end, return shortest distance and path to end
            if current_vertex == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                print("Shortest distance: " + str(distances[end]) + "\nShortest path: " + str(path))
                return distances[end]

            # go through neighbors of current vertex
            for neighbor in self.mainDictOfLists[current_vertex]:

                neighbor_vertex = neighbor['vertex']
                neighbor_distance = neighbor['distance']
                
                # find the distance from neighbor to start through base vertex
                shortestDistance = distances[current_vertex] + neighbor_distance

                # if the distance above is less than the previous recorded distance
                if shortestDistance < distances[neighbor_vertex]:
                    # set the recorded distance to the new distance
                    distances[neighbor_vertex] = shortestDistance
                    # set the previous fo the neighbor to the current
                    previous[neighbor_vertex] = current_vertex
                    # enque the neighbor with the new distance
                    priorityQ.enqueue(neighbor_vertex, distances[neighbor_vertex])
            
            # to see priorityQ while running
            # print(priorityQ)






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
g.add_update_edge("D", "F", 1)
g.add_update_edge("E", "F", 1)

# print(g)
g.dijkstra('A', 'E')