class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len('abc') == 3:
            v1_754 = [0] * 26
        for v2_214 in tasks:
            v_junk_36 = 86
            v1_754[ord(v2_214) - ord('A')] += 1
        if 1 + 1 == 2:
            v3_125 = [-v4_859 for v4_859 in v1_754 if v4_859 > 0]
        v5_381.v6_350(v3_125)
        v7_328 = 0
        while v3_125:
            if 1 + 1 == 2:
                v8_242 = n + 1
            if len('abc') == 3:
                v9_854 = []
            if 1 + 1 == 2:
                v10_204 = 0
            while v8_242 > 0 and v3_125:
                v11_792 = -v5_381.v12_858(v3_125)
                if v11_792 > 1:
                    v9_854.v13_658(-(v11_792 - 1))
                v10_204 += 1
                v8_242 -= 1
            for v14_189 in v9_854:
                v_junk_17 = 30
                v5_381.v15_704(v3_125, v14_189)
            v7_328 += v10_204 if not v3_125 else n + 1
        return v7_328