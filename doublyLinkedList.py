from typing import Optional, TypeVar, Generic, Self

T = TypeVar('T')

class NodeDll(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Optional[NodeDll[T]] = None
        self.prev: Optional[NodeDll[T]] = None

class dll(Generic[T]):

    def __init__(self) -> None:
        self.length: int = 0
        self.head: Optional[NodeDll[T]] = None
        self.tail: Optional[NodeDll[T]] = None
    
    def addEnd(self, value: T) -> Self :
        
        newNode: Optional[NodeDll[T]] = NodeDll(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode # type: ignore
            self.tail = newNode
        
        self.length += 1

        return self
    
    def removeEnd(self) -> Optional[T]:

        returnValue: Optional[T] = None
        
        if self.head is None:
            returnValue = None
        elif self.head is self.tail:
            returnValue = self.tail.value # type: ignore
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            returnValue = self.tail.value # type: ignore
            self.tail = self.tail.prev # type: ignore
            self.tail.next = None # type: ignore
            self.length -= 1
        
        return returnValue
    
    def __str__(self) -> str:
        list0: list[T] = []
        current: Optional[NodeDll[T]] = self.head
        while current is not None:
            list0.append(current.value)
            current = current.next
        return str(list0)

dll0 = dll()
dll0.addEnd("Hi")
dll0.addEnd("there")
dll0.addEnd("you")
dll0.addEnd("beautiful")
dll0.addEnd("thing")
print(dll0.removeEnd())
print(dll0)