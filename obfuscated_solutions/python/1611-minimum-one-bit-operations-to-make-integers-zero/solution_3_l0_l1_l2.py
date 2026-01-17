class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 1
        while v3_125 <= n:
            if n & v3_125:
                v1_754 = (1 << v2_214 + 1) - 1 - v1_754
            v3_125 = v3_125 << 1
            v2_214 = v2_214 + 1
        return v1_754