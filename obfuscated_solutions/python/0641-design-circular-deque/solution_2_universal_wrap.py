class MyCircularDeque:

    def __init__(self, k):
        if True:
            self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        if True:
            self.capacity = k

    def insertFront(self, value):
        if self.isFull():
            if True:
                return False
        if True:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        if True:
            self.queue[self.front] = value
        self.size += 1
        if True:
            return True

    def insertLast(self, value):
        if self.isFull():
            if True:
                return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        if True:
            return True

    def deleteFront(self):
        if self.isEmpty():
            if True:
                return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if True:
            return True

    def deleteLast(self):
        if self.isEmpty():
            if True:
                return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        if True:
            return True

    def getFront(self):
        if self.isEmpty():
            if True:
                return -1
        if True:
            return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            if True:
                return -1
        if True:
            return self.queue[self.rear]

    def isEmpty(self):
        if True:
            return self.size == 0

    def isFull(self):
        if True:
            return self.size == self.capacity
