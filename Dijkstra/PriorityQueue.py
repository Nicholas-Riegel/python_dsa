class PriorityQueue:

    def __init__(self):
        self.minBHList = []
    
    def __str__(self):
        return str(self.minBHList)
    
    def enqueue(self, value, priority):
        self.minBHList.append({"vertex": value, "distance": priority})
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

    def dequeue(self):

        # Guard
        if len(self.minBHList) == 0:
            return None
        if len(self.minBHList) < 3:
            return self.minBHList.pop(0)
        
        # wap first and last values
        self.swap(0, len(self.minBHList) - 1)
        
        # remove last value
        item = self.minBHList.pop()
        
        # Rearrange
        self.sinkDown(0)

        # return removed value
        return item
    
    # Helper function for dequeue
    # Recursively rearrange heap
    def sinkDown(self, parentIndex):

        # get child index
        childIndex = self.lowestPriorityChildIndex(parentIndex)
        
        # guard
        if childIndex is None: 
            return
        
        # get priorities
        parentPriority = self.minBHList[parentIndex]["distance"]
        childPriority = self.minBHList[childIndex]["distance"]

        #  if child priority is less than parent priority
        if childPriority < parentPriority:
            # swap parent and child values
            self.swap(parentIndex, childIndex)
            # run method again on new index
            self.sinkDown(childIndex)
    
    # Helper function for sinkDown()
    # find index of lowest (highest) priority child or return null
    def lowestPriorityChildIndex(self, parentIndex):
        
        # Get the child indexes
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        # if both are ob, return null
        if leftChildIndex >= len(self.minBHList): 
            return None
        
        # if only right is ob, return left
        elif rightChildIndex >= len(self.minBHList): 
            return leftChildIndex
        
        # if both are in bounds, return the index of larger value
        else:

            leftChildPriority = self.minBHList[leftChildIndex]["distance"]
            rightChildPriority = self.minBHList[rightChildIndex]["distance"]

            if leftChildPriority < rightChildPriority: 
                return leftChildIndex
            else: 
                return rightChildIndex