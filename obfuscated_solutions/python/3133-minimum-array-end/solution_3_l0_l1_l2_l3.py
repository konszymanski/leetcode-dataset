class Solution:

    def minEnd(self, n: int, x: int) -> int:
        v1_259 = x
        n = n - 1
        v2_320 = 1
        while n > 0:
            if v2_320 & x == 0:
                v1_259 = v1_259 | (n & 1) * v2_320
                n = n >> 1
            v2_320 = v2_320 << 1
        return v1_259