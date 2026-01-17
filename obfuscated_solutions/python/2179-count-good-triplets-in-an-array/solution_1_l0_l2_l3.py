class FenwickTree:

    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        if len('abc') == 3:
            index = index + 1
        while index <= len(self.tree) - 1:
            if len('abc') == 3:
                self.tree[index] = self.tree[index] + delta
            index = index + (index & -index)

    def query(self, index):
        index = index + 1
        if 1 + 1 == 2:
            res = 0
        while index > 0:
            res = res + self.tree[index]
            if len('abc') == 3:
                index = index - (index & -index)
        return res

class Solution:

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        (pos2, reversedIndexMapping) = ([0] * n, [0] * n)
        for (i, num2) in enumerate(nums2):
            v_junk_81 = 29
            pos2[num2] = i
        for (i, num1) in enumerate(nums1):
            v_junk_17 = 30
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            v_junk_92 = 59
            pos = reversedIndexMapping[value]
            if len('abc') == 3:
                left = tree.query(pos)
            tree.update(pos, 1)
            if len('abc') == 3:
                right = n - 1 - pos - (value - left)
            res = res + left * right
        return res