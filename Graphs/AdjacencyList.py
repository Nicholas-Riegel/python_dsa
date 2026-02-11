class AdjacencyList:

    # constructor
    # creates the dictionary
    def __init__(self):
        self.adjacencyListSet = {}

    # to string method
    # returns the stringified dictionary
    def __str__(self):
        return str(self.adjacencyListSet)

    # add vertex method
    def add_vertex(self, vertex):
        if vertex not in self.adjacencyListSet:
            self.adjacencyListSet[vertex] = set()

    # add edge method
    def add_edge(self, v1, v2):
        if v1 not in self.adjacencyListSet:
            self.add_vertex(v1)
        if v2 not in self.adjacencyListSet:
            self.add_vertex(v2)

        self.adjacencyListSet[v1].add(v2)
        self.adjacencyListSet[v2].add(v1)

    # has edge between two verticies check method
    def have_edge(self, v1, v2):
        if v1 not in self.adjacencyListSet or v2 not in self.adjacencyListSet:
            return False
        return v1 in self.adjacencyListSet[v2]
        
    # remove edge method
    def remove_edge(self, v1, v2):
        if self.have_edge(v1, v2):
            self.adjacencyListSet[v1].discard(v2)
            self.adjacencyListSet[v2].discard(v1)
            return True
        else:
            return False
        
    # remove vertext method
    def remove_vertex(self, vertex):
        if vertex not in self.adjacencyListSet:
            return False
        
        for v in self.adjacencyListSet[vertex]:
            self.adjacencyListSet[v].discard(vertex)
        
        del self.adjacencyListSet[vertex]
        return True
        
    # get verticies method
    def get_vertices(self):
        return list(self.adjacencyListSet.keys())


al = AdjacencyList()
al.add_vertex("Hello")
al.add_edge("Hello", "World")
print(al.have_edge("Hello", "World"))
print(al.get_vertices())
print(al)