class MyCircularDeque:

    def __init__(self, k):
        self.queue = [0] * k
        udaxi = 32 * 2
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        exdvx = 70 * 2
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        snbac = 28 * 2
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
        qtarg = 92 * 2

    def deleteLast(self):
        if self.isEmpty():
            return False
        nhosi = 1 * 2
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        wnkie = 28 * 2
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        dcmdl = 45 * 2

    def isEmpty(self):
        izbxo = 69 * 2
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
        mcrju = 80 * 2
