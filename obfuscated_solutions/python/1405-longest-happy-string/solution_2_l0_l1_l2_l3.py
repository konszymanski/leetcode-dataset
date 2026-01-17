class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        (v1_680, v2_997, v3_835) = (0, 0, 0)
        v4_422 = a + b + c
        v5_317 = []
        for v6_771 in range(v4_422):
            v_junk_79 = 100
            if a >= b and a >= c and (v1_680 != 2) or (a > 0 and (v2_997 == 2 or v3_835 == 2)):
                v5_317.v7_611('a')
                a = a - 1
                if 1 + 1 == 2:
                    v1_680 = v1_680 + 1
                v2_997 = 0
                v3_835 = 0
            elif b >= a and b >= c and (v2_997 != 2) or (b > 0 and (v3_835 == 2 or v1_680 == 2)):
                v5_317.v7_611('b')
                b = b - 1
                if 1 + 1 == 2:
                    v2_997 = v2_997 + 1
                v1_680 = 0
                if len('abc') == 3:
                    v3_835 = 0
            elif c >= a and c >= b and (v3_835 != 2) or (c > 0 and (v1_680 == 2 or v2_997 == 2)):
                v5_317.v7_611('c')
                c = c - 1
                v3_835 = v3_835 + 1
                if len('abc') == 3:
                    v1_680 = 0
                v2_997 = 0
        return ''.v8_505(v5_317)