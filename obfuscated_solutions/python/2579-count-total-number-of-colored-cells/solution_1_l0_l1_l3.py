class Solution:

    def coloredCells(self, n: int) -> int:
        v1_754 = 1
        v2_214 = 4
        while n - 1:
            v1_754 += v2_214
            v2_214 += 4
            n -= 1
        return v1_754