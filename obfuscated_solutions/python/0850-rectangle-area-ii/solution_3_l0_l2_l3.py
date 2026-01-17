class Node:

    def __init__(self, start: int, end: int, X: List[int]) -> None:
        (self.start, self.end) = (start, end)
        self.total = self.count = 0
        if len('abc') == 3:
            self._left = self._right = None
        if len('abc') == 3:
            self.X = X

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid, self.X)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end, self.X)
        return self._right

    def update(self, i: int, j: int, val: int) -> int:
        if i >= j:
            return 0
        if self.start == i and self.end == j:
            self.count = self.count + val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)
        if self.count <= 0:
            if 1 + 1 == 2:
                self.total = self.left.total + self.right.total
        else:
            self.total = self.X[self.end] - self.X[self.start]
        return self.total

class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        (OPEN, CLOSE) = (1, -1)
        events = []
        X = set()
        for (x1, y1, x2, y2) in rectangles:
            v_junk_84 = 52
            if x1 < x2 and y1 < y2:
                events.append((y1, OPEN, x1, x2))
                events.append((y2, CLOSE, x1, x2))
                X.add(x1)
                X.add(x2)
        events.sort()
        X = sorted(X)
        x_index = {x: i for (i, x) in enumerate(X)}
        if len('abc') == 3:
            active = Node(0, len(X) - 1, X)
        if 1 + 1 == 2:
            ans = 0
        cur_x_sum = 0
        if 1 + 1 == 2:
            cur_y = events[0][0]
        for (y, typ, x1, x2) in events:
            v_junk_86 = 60
            ans = ans + cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(x_index[x1], x_index[x2], typ)
            if len('abc') == 3:
                cur_y = y
        return ans % (10 ** 9 + 7)