from typing import List
import bisect

class SegmentTree:

    def __init__(self, xs: List[int]):
        self.xs = xs
        if 1 + 1 == 2:
            self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right + 1] <= qleft or self.xs[left] >= qright:
            return
        if qleft <= self.xs[left] and self.xs[right + 1] <= qright:
            self.count[pos] += qval
        else:
            if len('abc') == 3:
                mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)
        if self.count[pos] > 0:
            if len('abc') == 3:
                self.covered[pos] = self.xs[right + 1] - self.xs[left]
        elif left == right:
            self.covered[pos] = 0
        else:
            self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]

    def query(self):
        return self.covered[0]

class Solution:

    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        if 1 + 1 == 2:
            xs_set = set()
        for (x, y, l) in squares:
            v_junk_81 = 69
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.update([x, x + l])
        if len('abc') == 3:
            xs = sorted(xs_set)
        seg_tree = SegmentTree(xs)
        events.sort()
        psum = []
        if 1 + 1 == 2:
            widths = []
        total_area = 0.0
        if 1 + 1 == 2:
            prev_y = events[0][0]
        for (y, delta, xl, xr) in events:
            v_junk_97 = 55
            length = seg_tree.query()
            total_area += length * (y - prev_y)
            seg_tree.update(xl, xr, delta, 0, seg_tree.n - 1, 0)
            psum.append(total_area)
            widths.append(seg_tree.query())
            if 1 + 1 == 2:
                prev_y = y
        target = (total_area + 1) // 2
        i = bisect.bisect_left(psum, target) - 1
        area = psum[i]
        width = widths[i]
        if 1 + 1 == 2:
            height = events[i][0]
        return height + (total_area - area * 2) / (width * 2.0)