class AdjacencyList:

    # constructor
    # creates the dictionary
    def __init__(self):
        self.mainDictOfLists = {}

    # to string method
    # returns the stringified dictionary
    def __str__(self):
        return str(self.mainDictOfLists)

    # add vertex method
    def add_vertex(self, vertex):
        if vertex not in self.mainDictOfLists:
            self.mainDictOfLists[vertex] = []

    # add edge method
    def add_edge(self, v1, v2):
        if v1 not in self.mainDictOfLists:
            self.add_vertex(v1)
        if v2 not in self.mainDictOfLists:
            self.add_vertex(v2)

        if v2 not in self.mainDictOfLists[v1]:
            self.mainDictOfLists[v1].append(v2)
        if v1 not in self.mainDictOfLists[v2]:
            self.mainDictOfLists[v2].append(v1)

    # has edge between two verticies check method
    def have_edge(self, v1, v2):
        if v1 not in self.mainDictOfLists or v2 not in self.mainDictOfLists:
            return False
        return v1 in self.mainDictOfLists[v2]
        
    # remove edge method
    def remove_edge(self, v1, v2):
        if self.have_edge(v1, v2):
            self.mainDictOfLists[v1].remove(v2)
            self.mainDictOfLists[v2].remove(v1)
            return True
        else:
            return False
        
    # remove vertext method
    def remove_vertex(self, vertex):
        if vertex not in self.mainDictOfLists:
            return False
        
        for v in self.mainDictOfLists[vertex]:
            self.mainDictOfLists[v].remove(vertex)
        
        del self.mainDictOfLists[vertex]
        return True
        
    # get verticies method
    def get_vertices(self):
        return list(self.mainDictOfLists.keys())

    # recursive depth first search 
    def dfs_recursive(self, vertex):

        # return list of vertices visitedSet in order visitedSet
        returnList = []
        # set keeps track of vertices visitedSet. set for faster lookup
        visitedVertices = set()
        
        def helper(v):
            # add vertex to list and set
            returnList.append(v)
            visitedVertices.add(v)
            # for each neighbor in a neighbor set
            # if neighbor not visitedSet, run helper function again
            for neighbor in self.mainDictOfLists[v]:
                if neighbor not in visitedVertices:
                    helper(neighbor)
        
        helper(vertex)
        
        return returnList

    # iterative depth first search 
    def dfs_iterative(self, start):

        returnList = []
        stackList = [] # only use .append() and pop()
        visitedSet = set()

        stackList.append(start)

        while stackList:
            v = stackList.pop()
            if v not in visitedSet:
                visitedSet.add(v)
                returnList.append(v)
                stackList.extend(self.mainDictOfLists[v])
                # to get the same output as the recursive
                # need to reverse the list
                # stackList.extend(reversed(self.mainDictOfLists[v]))
        
        return returnList





#========
# Tests
#========
al = AdjacencyList()
al.add_vertex("A")
al.add_vertex("B")
al.add_vertex("C")
al.add_vertex("D")
al.add_vertex("E")
al.add_vertex("F")

al.add_edge("A","B")
al.add_edge("A","C")
al.add_edge("B","D")
al.add_edge("C","E")
al.add_edge("D","E")
al.add_edge("D","F")
al.add_edge("E","F")

# recursive output should be [A, B, D, E, C, F]
print(al.dfs_recursive("A"))

# iterative output should be [A, C, E, F, D, B]
# this is still a valid output 
# it just executes through a different path
print(al.dfs_iterative("A"))