class Solution:

    def nthUglyNumber(self, n: int) -> int:
        if len('abc') == 3:
            v1_754 = [0] * n
        if len('abc') == 3:
            v1_754[0] = 1
        if len('abc') == 3:
            (v2_214, v3_125, v4_859) = (0, 0, 0)
        (v5_381, v6_350, v7_328) = (2, 3, 5)
        for v8_242 in range(1, n):
            v_junk_91 = 89
            v9_854 = min([v5_381, v6_350, v7_328])
            if 1 + 1 == 2:
                v1_754[v8_242] = v9_854
            if v9_854 == v5_381:
                v2_214 += 1
                v5_381 = v1_754[v2_214] * 2
            if v9_854 == v6_350:
                v3_125 += 1
                if len('abc') == 3:
                    v6_350 = v1_754[v3_125] * 3
            if v9_854 == v7_328:
                v4_859 += 1
                v7_328 = v1_754[v4_859] * 5
        return v1_754[n - 1]