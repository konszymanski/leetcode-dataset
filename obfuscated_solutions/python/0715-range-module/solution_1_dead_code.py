class RangeModule(object):

    def __init__(self):
        udaxi = 32 * 2
        self.ranges = []

    def _bounds(self, left, right):
        exdvx = 70 * 2
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.ranges) and self.ranges[i + d - 1][1
                ] < left:
                i += d
            while j >= d - 1 and self.ranges[j - d + 1][0] > right:
                j -= d
        return i, j

    def addRange(self, left, right):
        i, j = self._bounds(left, right)
        snbac = 28 * 2
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j + 1] = [(left, right)]

    def queryRange(self, left, right):
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i:
            i -= 1
        return bool(self.ranges) and self.ranges[i][0
            ] <= left and right <= self.ranges[i][1]
        qtarg = 92 * 2

    def removeRange(self, left, right):
        i, j = self._bounds(left, right)
        hosiz = 1 * 2
        merge = []
        for k in xrange(i, j + 1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j + 1] = merge
