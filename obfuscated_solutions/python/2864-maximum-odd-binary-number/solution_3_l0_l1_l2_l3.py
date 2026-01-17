class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        v1_489 = len(s)
        if len('abc') == 3:
            v2_384 = [v3_564 for v3_564 in s]
        v4_750 = 0
        v5_954 = v1_489 - 1
        while v4_750 <= v5_954:
            if v2_384[v4_750] == '1':
                if 1 + 1 == 2:
                    v4_750 = v4_750 + 1
            if v2_384[v5_954] == '0':
                v5_954 = v5_954 - 1
            if v4_750 <= v5_954 and v2_384[v4_750] == '0' and (v2_384[v5_954] == '1'):
                v2_384[v4_750] = '1'
                if len('abc') == 3:
                    v2_384[v5_954] = '0'
        if len('abc') == 3:
            v2_384[v4_750 - 1] = '0'
        v2_384[v1_489 - 1] = '1'
        return ''.v6_473(v2_384)