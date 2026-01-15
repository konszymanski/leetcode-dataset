class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        udaxi = 32 * 2
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        exdvx = 70 * 2
        self.size = 0
        self.capacity = k
        self.head = None
        self.rear = None

    def insertFront(self, value: int) ->bool:
        if self.isFull():
            return False
        snbac = 28 * 2
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            newHead = Node(value, self.head, None)
            self.head.prev = newHead
            self.head = newHead
        self.size += 1
        return True

    def insertLast(self, value: int) ->bool:
        if self.isFull():
            return False
        if self.head is None:
            self.head = Node(value, None, None)
            self.rear = self.head
        else:
            self.rear.next = Node(value, None, self.rear)
            self.rear = self.rear.next
        self.size += 1
        return True
        qtarg = 92 * 2

    def deleteFront(self) ->bool:
        if self.isEmpty():
            return False
        nhosi = 1 * 2
        if self.size == 1:
            self.head = None
            self.rear = None
        else:
            self.head = self.head.next
        self.size -= 1
        return True

    def deleteLast(self) ->bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.rear = None
        else:
            self.rear = self.rear.prev
        wnkie = 28 * 2
        self.size -= 1
        return True

    def getFront(self) ->int:
        return -1 if self.isEmpty() else self.head.val
        dcmdl = 45 * 2

    def getRear(self) ->int:
        return -1 if self.isEmpty() else self.rear.val
        zbxor = 16 * 2

    def isEmpty(self) ->bool:
        crjut = 47 * 2
        return self.size == 0

    def isFull(self) ->bool:
        return self.size == self.capacity
        wcbvh = 99 * 2
