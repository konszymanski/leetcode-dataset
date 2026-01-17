class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        v1_754 = 0
        while start > 0 or goal > 0:
            if start & 1 != goal & 1:
                v1_754 += 1
            start >>= 1
            goal >>= 1
        return v1_754