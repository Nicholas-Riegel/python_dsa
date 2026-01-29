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
    
    # Get at index
    def getAt(self, i):
    
        if self.head is None:
            raise IndexError("List is empty.")
        if i >= self.length or i < 0:
            raise IndexError("Index out of bounds.")
        
        if i < self.length // 2:
            current = self.head
            for _ in range(i):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - i):
                current = current.prev
            
        return current.value 
    
    # Set at index
    def setAt(self, i, value):
        
        if self.head is None:
            raise IndexError("List is empty.")
        if i >= self.length or i < 0:
            raise IndexError("Index out of bounds.")
        
        if i < self.length // 2:
            current = self.head
            for _ in range(i):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - i):
                current = current.prev

        current.value = value
        return self
    
    # Insert at index
    def insertAt(self, i, value):
        
        if self.head is None or i >= self.length:
            self.addEnd(value)
            return self
        elif i <= 0:
            self.addFront(value)
            return self
        elif i < self.length // 2:
            current = self.head
            for _ in range(i):
                current = current.next 
        else:
            current = self.tail
            for _ in range(self.length - 1 - i):
                current = current.prev
        
        newNode = NodeDLL(value)
        newNode.prev = current.prev
        newNode.next = current 
        current.prev.next = newNode 
        current.prev = newNode

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
        elif i < self.length // 2:
            current = self.head
            for _ in range(i):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1 - i):
                current = current.prev
        
        current.prev.next = current.next 
        current.next.prev = current.prev

        self.length -= 1

        return current.value 

    # Reverse
    
    def __str__(self):
        list_0 = []
        current = self.head
        while current is not None:
            list_0.append(current.value)
            current = current.next
        return str(list_0)


dll_0 = DLL()
dll_0.addEnd("Hi")
dll_0.addEnd("there")
dll_0.addEnd("you")
dll_0.addEnd("beautiful")
dll_0.addEnd("thing")
print(dll_0.removeAt(0))
print(dll_0)
print(dll_0.length)
