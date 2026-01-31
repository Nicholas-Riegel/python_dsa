class NodeDLL:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        list_0 = []
        current = self.head
        while current is not None:
            list_0.append(current.value)
            current = current.next
        return str(list_0)
    
    def addEnd(self, value):
        
        newNode = NodeDLL(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1

        return self
    
    def removeEnd(self):
        
        if self.head is None:
            raise IndexError("List is empty.")
        elif self.head is self.tail:
            returnValue = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            returnValue = self.tail.value 
            self.tail = self.tail.prev
            self.tail.next = None 
            self.length -= 1
        
        return returnValue
    
    # Add to front
    def addFront(self, value):

        newNode = NodeDLL(value)
        
        self.head.prev = newNode 
        newNode.next = self.head 
        self.head = newNode
        self.length += 1
        
        return self
    
    # Remove from front
    def removeFront(self):
        
        if self.head is None:
            raise IndexError("List is empty.")
        elif self.head is self.tail:
            returnValue = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            returnValue = self.head.value
            self.head = self.head.next
            self.head.prev = None 
            self.length -= 1

        return returnValue
    
    def findAt(self, i):

        if i < self.length // 2:
            current = self.head
            for _ in range(i):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - i):
                current = current.prev

        return current
    
    # Get at index
    def getAt(self, i):
    
        if self.head is None:
            raise IndexError("List is empty.")
        elif i >= self.length or i < 0:
            raise IndexError("Index out of bounds.")
        else:
            current = self.findAt(i)
            
        return current.value 
    
    # Set at index
    def setAt(self, i, value):
        
        if self.head is None:
            raise IndexError("List is empty.")
        elif i >= self.length or i < 0:
            raise IndexError("Index out of bounds.")
        else:
            current = self.findAt(i)
            current.value = value
        
        return self
    
    # Insert at index
    def insertAt(self, i, value):
        
        if (i < 0 or i >= self.length):
            raise IndexError("Index out of bounds.")
        elif i == 0: 
            self.addFront(value)
        elif i == self.length - 1:
            self.addEnd(value)
        else:
            newNode = NodeDLL(value)
            oldNode = self.findAt(i)

            newNode.prev = oldNode.prev
            newNode.next = oldNode 
            oldNode.prev.next = newNode 
            oldNode.prev = newNode

            self.length += 1

        return self
    
    # Remove at index
    def removeAt(self, i):
        
        if self.head is None:
            raise IndexError("List is empty.")            
        elif i >= self.length or i < 0:
            raise IndexError("Index out of bounds.")            
        elif i == 0:
            return self.removeFront()
        elif i == self.length - 1:
            return self.removeEnd()
        else:
            targetNode = self.findAt(i)
            targetNode.prev.next = targetNode.next 
            targetNode.next.prev = targetNode.prev
            self.length -= 1
            return targetNode.value 

    # Reverse
    def reverse(self):

        prev = None
        current = self.head
        next = None
    
        while (current is not None):

            next = current.next

            current.next = prev
            current.prev = next

            prev = current
            current = next

        self.head, self.tail = self.tail, self.head
        
        return self


dll_0 = DLL()
dll_0.addEnd("Hi")
dll_0.addEnd("there")
dll_0.addEnd("you")
dll_0.addEnd("beautiful")
dll_0.addEnd("thing")
print(dll_0.reverse())
