class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        (v1_754, v2_214, v3_125) = (0, 0, 0)
        v4_859 = a + b + c
        v5_381 = []
        for v6_350 in range(v4_859):
            if a >= b and a >= c and (v1_754 != 2) or (a > 0 and (v2_214 == 2 or v3_125 == 2)):
                v5_381.v7_328('a')
                a = a - 1
                v1_754 = v1_754 + 1
                v2_214 = 0
                v3_125 = 0
            elif b >= a and b >= c and (v2_214 != 2) or (b > 0 and (v3_125 == 2 or v1_754 == 2)):
                v5_381.v7_328('b')
                b = b - 1
                v2_214 = v2_214 + 1
                v1_754 = 0
                v3_125 = 0
            elif c >= a and c >= b and (v3_125 != 2) or (c > 0 and (v1_754 == 2 or v2_214 == 2)):
                v5_381.v7_328('c')
                c = c - 1
                v3_125 = v3_125 + 1
                v1_754 = 0
                v2_214 = 0
        return ''.v8_242(v5_381)