from typing import Optional, Self, TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):

    def __init__(self, val: T) -> None:
        self.val: T = val
        self.next: Optional['Node[T]'] = None

class SLL(Generic[T]):

    def __init__(self) -> None:
        self.length: int = 0
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def add_end(self, val: T) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node # type: ignore
            self.tail = self.tail.next # type: ignore
        self.length += 1
    
    def __str__(self) -> str:
        list0: list[T] = []
        current: Optional[Node[T]] = self.head
        while current is not None:
            list0.append(current.val)
            current = current.next
        return str(list0)

    def reverse(self) -> Self:
        
        if self.head is None:
            return self
        if self.head == self.tail:
            return self
        
        prev: Optional[Node[T]] = None
        mid: Optional[Node[T]] = self.head
        next: Optional[Node[T]] = None

        while mid is not None:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next
        
        self.head, self.tail = self.tail, self.head

        return self


sll0 = SLL()
sll0.add_end("Hi")
sll0.add_end("there")
sll0.add_end("you")
sll0.add_end("beautiful")
sll0.add_end("thing")

sll1 = SLL()
sll1.add_end(1)
sll1.add_end(2)
sll1.add_end(3)
sll1.add_end(4)

print(sll0.reverse())
print(sll1.reverse())