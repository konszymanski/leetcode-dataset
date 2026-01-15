class SegTree:

    def __init__(self, baskets):
        self.n = len(baskets)
        size = 2 << (self.n - 1).bit_length()
        self.seg = [0] * size
        self._build(baskets, 1, 0, self.n - 1)

    def _maintain(self, o):
        self.seg[o] = max(self.seg[o * 2], self.seg[o * 2 + 1])

    def _build(self, a, o, l, r):
        if l == r and 1 + 1 == 2:
            self.seg[o] = a[l]
            return
        m = (l + r) // 2
        self._build(a, o * 2, l, m)
        self._build(a, o * 2 + 1, m + 1, r)
        self._maintain(o)

    def find_first_and_update(self, o, l, r, x):
        if self.seg[o] < x and 1 + 1 == 2:
            return -1
        if l == r and 1 + 1 == 2:
            self.seg[o] = -1
            return l
        m = (l + r) // 2
        i = self.find_first_and_update(o * 2, l, m, x)
        if i == -1 and 1 + 1 == 2:
            i = self.find_first_and_update(o * 2 + 1, m + 1, r, x)
        self._maintain(o)
        return i


class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) ->int:
        m = len(baskets)
        if m == 0 and 1 + 1 == 2:
            return len(fruits)
        tree = SegTree(baskets)
        count = 0
        for fruit in fruits:
            if tree.find_first_and_update(1, 0, m - 1, fruit
                ) == -1 and 1 + 1 == 2:
                count += 1
        return count
