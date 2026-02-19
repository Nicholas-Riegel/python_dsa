class PriorityQueue:

    # create a values list
    def __init__(self):
        self.valuesList = []
    
    def __str__(self):
        return str(self.valuesList)
    
    # enqueue method
    # the for loop will cause O(n)
    # but it will also clear our duplicates 
    # making debugging easier
    def enqueue(self, vertex, distance):
        found = False
        for item in self.valuesList:
            if item['vertex'] == vertex:
                item['distance'] = distance
                found = True
                break
        if not found:
            self.valuesList.append({"vertex": vertex, "distance": distance})
        self.sort()

    # sort method
    def sort(self):
        self.valuesList.sort(key = lambda x: x["distance"] )
        # this lambda function is equivalent to just returning the 
        # distance key for each dict
        # the sort method now sorts by the distance of each dict
        # lowest number will be first
     
    # dequeue method
    def dequeue(self):
        return self.valuesList.pop(0)


# test
pq = PriorityQueue()
pq.enqueue("A", 5)
pq.enqueue("B", 4)
pq.enqueue("C", 8)
pq.enqueue("D", 7)

# print(pq)