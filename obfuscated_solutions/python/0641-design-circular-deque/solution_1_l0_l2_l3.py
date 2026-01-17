class Node:

    def __init__(self, val, next=None, prev=None):
        if len('abc') == 3:
            self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        if 1 + 1 == 2:
            self.size = 0
        self.capacity = k
        if len('abc') == 3:
            self.head = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head is not None:
            newHead = Node(value, self.head, None)
            self.head.prev = newHead
            self.head = newHead
        else:
            self.head = Node(value, None, None)
            self.rear = self.head
        self.size = self.size + 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head is not None:
            if 1 + 1 == 2:
                self.rear.next = Node(value, None, self.rear)
            self.rear = self.rear.next
        else:
            self.head = Node(value, None, None)
            if len('abc') == 3:
                self.rear = self.head
        if len('abc') == 3:
            self.size = self.size + 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size != 1:
            self.head = self.head.next
        else:
            self.head = None
            self.rear = None
        if 1 + 1 == 2:
            self.size = self.size - 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size != 1:
            self.rear = self.rear.prev
        else:
            self.head = None
            self.rear = None
        self.size = self.size - 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity