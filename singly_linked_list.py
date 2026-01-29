class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_end(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1
    
    def __str__(self):
        list0 = []
        current = self.head
        while current is not None:
            list0.append(current.val)
            current = current.next
        return str(list0)

    def reverse(self):
        
        if self.head is None:
            return self
        if self.head is self.tail:
            return self
        
        prev = None
        mid = self.head
        next = None

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