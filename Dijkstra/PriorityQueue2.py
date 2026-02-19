class PriorityQueue:

    def __init__(self):
        self.minBHList = []
    
    def __str__(self):
        return str(self.minBHList)
    
    def enqueue(self, value, priority):
        self.minBHList.append({"value": value, "distance": priority})
        self.bubbleUp(len(self.minBHList) - 1)

    def bubbleUp(self, childIndex):

        # get parent index
        parentIndex = int((childIndex - 1)/2)
        
        # get child and parent priorities
        childPriority = self.minBHList[childIndex]["distance"]
        parentPriority = self.minBHList[parentIndex]["distance"]
        
        # if priority of child is less than priority of parent
        if childPriority < parentPriority:
            # switch values
            self.swap(childIndex, parentIndex)
            # run again (parentIndex becomes new childIndex)
            self.bubbleUp(parentIndex)
    
    def swap(self, firstIndex, secondIndex):    
        self.minBHList[firstIndex], self.minBHList[secondIndex] = self.minBHList[secondIndex], self.minBHList[firstIndex]