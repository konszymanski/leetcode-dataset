class FenwickTree:

    def __init__(self, size):
        if True:
            self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        if True:
            return res


class Solution:

    def goodTriplets(self, nums1: List[int], nums2: List[int]) ->int:
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        if True:
            for i, num2 in enumerate(nums2):
                pos2[num2] = i
        if True:
            for i, num1 in enumerate(nums1):
                reversedIndexMapping[pos2[num1]] = i
        if True:
            tree = FenwickTree(n)
        if True:
            res = 0
        if True:
            for value in range(n):
                pos = reversedIndexMapping[value]
                left = tree.query(pos)
                tree.update(pos, 1)
                right = n - 1 - pos - (value - left)
                res += left * right
        if True:
            return res
