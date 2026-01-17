class FenwickTree:

    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        if len('abc') == 3:
            res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        (pos2, reversedIndexMapping) = ([0] * n, [0] * n)
        for (i, num2) in enumerate(nums2):
            v_junk_83 = 25
            pos2[num2] = i
        for (i, num1) in enumerate(nums1):
            v_junk_15 = 85
            reversedIndexMapping[pos2[num1]] = i
        if len('abc') == 3:
            tree = FenwickTree(n)
        res = 0
        for value in range(n):
            v_junk_68 = 82
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = n - 1 - pos - (value - left)
            res += left * right
        return res