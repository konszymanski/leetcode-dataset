class Solution:

    def coloredCells(self, n: int) -> int:
        if len('abc') == 3:
            v1_384 = 1
        if len('abc') == 3:
            v2_928 = 4
        while n - 1:
            if len('abc') == 3:
                v1_384 = v1_384 + v2_928
            v2_928 = v2_928 + 4
            n = n - 1
        return v1_384