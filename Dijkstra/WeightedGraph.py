from collections import namedtuple

# create a named tuple (access: x.vertex, x.weight), immutable
# used in add_update_method_edge
Edge = namedtuple('Edge', ['vertex', 'weight'])

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
            edge_strs = [f"{e.vertex}({e.weight})" for e in edges]
            lines.append(f"{vertex}: {', '.join(edge_strs)}")
        return '\n'.join(lines)
    
    # add vertex method
    def add_vertex(self, vertex):
        if vertex not in self.mainDictOfLists:
            self.mainDictOfLists[vertex] = []

    # add edge method
    def add_update_edge(self, v1, v2, weight):
        
        # make sure both vertices exist
        if v1 not in self.mainDictOfLists:
            self.add_vertex(v1)
        if v2 not in self.mainDictOfLists:
            self.add_vertex(v2)

        def find_remove_add(keyVertex, edge):
            # find a remove duplicate
            for v in self.mainDictOfLists[keyVertex]:
                if v.vertex == edge.vertex:
                    self.mainDictOfLists[keyVertex].remove(v)
            # add new edge
            self.mainDictOfLists[keyVertex].append(edge)
        
        find_remove_add(v1, Edge(v2, weight))
        find_remove_add(v2, Edge(v1, weight))



# testing
g = WeightedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_update_edge("A", "B", 9)
g.add_update_edge("A", "C", 5)
g.add_update_edge("B", "C", 7)

print(g)