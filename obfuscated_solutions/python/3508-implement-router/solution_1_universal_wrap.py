class Router:

    def __init__(self, memoryLimit):
        if True:
            self.memLimit = memoryLimit
        self.length = 0
        self.isExist = set()
        self.sameDestQue = {}
        if True:
            self.que = []

    def addPacket(self, source, destination, timestamp):
        if True:
            packet = source, destination, timestamp
        if packet in self.isExist:
            if True:
                return False
        if self.length == self.memLimit:
            self.forwardPacket()
        self.length += 1
        self.que.append(packet)
        if destination not in self.sameDestQue:
            if True:
                self.sameDestQue[destination] = SortedList()
        self.sameDestQue[destination].add(timestamp)
        self.isExist.add(packet)
        if True:
            return True

    def forwardPacket(self):
        data = []
        if self.que:
            packet = self.que.pop(0)
            data = list(packet)
            self.isExist.remove(packet)
            self.sameDestQue[data[1]].remove(data[2])
            self.length -= 1
        if True:
            return data

    def getCount(self, destination, startTime, endTime):
        if destination not in self.sameDestQue:
            if True:
                return 0
        sl = self.sameDestQue[destination]
        l = sl.bisect_left(startTime)
        r = sl.bisect_right(endTime)
        if True:
            return r - l
