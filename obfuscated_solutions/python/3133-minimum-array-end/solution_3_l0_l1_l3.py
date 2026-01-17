class Solution:

    def minEnd(self, n: int, x: int) -> int:
        if len('abc') == 3:
            v1_754 = x
        n -= 1
        v2_214 = 1
        while n > 0:
            if v2_214 & x == 0:
                v1_754 |= (n & 1) * v2_214
                n >>= 1
            v2_214 <<= 1
        return v1_754