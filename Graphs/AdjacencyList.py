class AdjacencyList:

    # constructor
    # creates the dictionary
    def __init__(self):
        self.mainDictOfSets = {}

    # to string method
    # returns the stringified dictionary
    def __str__(self):
        return str(self.mainDictOfSets)

    # add vertex method
    # using set instead of list to optimize out duplicates
    def add_vertex(self, vertex):
        if vertex not in self.mainDictOfSets:
            self.mainDictOfSets[vertex] = set()

    # add edge method
    def add_edge(self, v1, v2):
        if v1 not in self.mainDictOfSets:
            self.add_vertex(v1)
        if v2 not in self.mainDictOfSets:
            self.add_vertex(v2)

        self.mainDictOfSets[v1].add(v2)
        self.mainDictOfSets[v2].add(v1)

    # has edge between two verticies check method
    def have_edge(self, v1, v2):
        if v1 not in self.mainDictOfSets or v2 not in self.mainDictOfSets:
            return False
        return v1 in self.mainDictOfSets[v2]
        
    # remove edge method
    def remove_edge(self, v1, v2):
        if self.have_edge(v1, v2):
            self.mainDictOfSets[v1].discard(v2)
            self.mainDictOfSets[v2].discard(v1)
            return True
        else:
            return False
        
    # remove vertext method
    def remove_vertex(self, vertex):
        if vertex not in self.mainDictOfSets:
            return False
        
        for v in self.mainDictOfSets[vertex]:
            self.mainDictOfSets[v].discard(vertex)
        
        del self.mainDictOfSets[vertex]
        return True
        
    # get verticies method
    def get_vertices(self):
        return list(self.mainDictOfSets.keys())


#========
# Tests
#========
al = AdjacencyList()
al.add_vertex("Hello")
al.add_edge("Hello", "World")
print(al.have_edge("Hello", "World"))
print(al.get_vertices())
print(al)