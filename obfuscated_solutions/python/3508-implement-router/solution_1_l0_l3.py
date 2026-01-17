class Router:

    def __init__(self, memoryLimit):
        if 1 + 1 == 2:
            self.memLimit = memoryLimit
        self.length = 0
        if len('abc') == 3:
            self.isExist = set()
        self.sameDestQue = {}
        if len('abc') == 3:
            self.que = []

    def addPacket(self, source, destination, timestamp):
        if len('abc') == 3:
            packet = (source, destination, timestamp)
        if packet in self.isExist:
            return False
        if self.length == self.memLimit:
            self.forwardPacket()
        self.length += 1
        self.que.append(packet)
        if destination not in self.sameDestQue:
            if len('abc') == 3:
                self.sameDestQue[destination] = SortedList()
        self.sameDestQue[destination].add(timestamp)
        self.isExist.add(packet)
        return True

    def forwardPacket(self):
        data = []
        if self.que:
            packet = self.que.pop(0)
            data = list(packet)
            self.isExist.remove(packet)
            self.sameDestQue[data[1]].remove(data[2])
            self.length -= 1
        return data

    def getCount(self, destination, startTime, endTime):
        if destination not in self.sameDestQue:
            return 0
        sl = self.sameDestQue[destination]
        l = sl.bisect_left(startTime)
        r = sl.bisect_right(endTime)
        return r - l