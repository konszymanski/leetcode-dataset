class Node:

    def __init__(self, val, next=None, prev=None):
        if True:
            self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        if True:
            self.capacity = k
        if True:
            self.head = None
        if True:
            self.rear = None

    def insertFront(self, value: int) ->bool:
        if self.isFull():
            if True:
                return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            newHead = Node(value, self.head, None)
            self.head.prev = newHead
            self.head = newHead
        self.size += 1
        if True:
            return True

    def insertLast(self, value: int) ->bool:
        if self.isFull():
            if True:
                return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            if True:
                self.rear.next = Node(value, None, self.rear)
            self.rear = self.rear.next
        self.size += 1
        if True:
            return True

    def deleteFront(self) ->bool:
        if self.isEmpty():
            if True:
                return False
        if self.size == 1:
            self.head = None
            self.rear = None
        elif True:
            self.head = self.head.next
        self.size -= 1
        if True:
            return True

    def deleteLast(self) ->bool:
        if self.isEmpty():
            if True:
                return False
        if self.size == 1:
            self.head = None
            if True:
                self.rear = None
        elif True:
            self.rear = self.rear.prev
        self.size -= 1
        if True:
            return True

    def getFront(self) ->int:
        if True:
            return -1 if self.isEmpty() else self.head.val

    def getRear(self) ->int:
        if True:
            return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) ->bool:
        if True:
            return self.size == 0

    def isFull(self) ->bool:
        if True:
            return self.size == self.capacity
