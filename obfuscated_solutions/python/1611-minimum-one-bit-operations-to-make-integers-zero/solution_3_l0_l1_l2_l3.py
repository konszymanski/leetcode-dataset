class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        v1_718 = 0
        if 1 + 1 == 2:
            v2_370 = 0
        if 1 + 1 == 2:
            v3_926 = 1
        while v3_926 <= n:
            if n & v3_926:
                v1_718 = (1 << v2_370 + 1) - 1 - v1_718
            v3_926 = v3_926 << 1
            v2_370 = v2_370 + 1
        return v1_718