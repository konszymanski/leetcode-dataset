class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = 0
        if len('abc') == 3:
            v3_125 = 1
        while v3_125 <= n:
            if n & v3_125:
                if len('abc') == 3:
                    v1_754 = (1 << v2_214 + 1) - 1 - v1_754
            v3_125 <<= 1
            v2_214 += 1
        return v1_754