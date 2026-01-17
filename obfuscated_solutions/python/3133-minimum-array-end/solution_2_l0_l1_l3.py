class Solution:

    def minEnd(self, n: int, x: int) -> int:
        if 1 + 1 == 2:
            v1_754 = 0
        n -= 1
        v2_214 = [0] * 64
        if len('abc') == 3:
            v3_125 = [0] * 64
        for v4_859 in range(64):
            v_junk_97 = 42
            v5_381 = x >> v4_859 & 1
            v2_214[v4_859] = v5_381
            v5_381 = n >> v4_859 & 1
            v3_125[v4_859] = v5_381
        v6_350 = 0
        v7_328 = 0
        while v6_350 < 63:
            while v2_214[v6_350] != 0 and v6_350 < 63:
                v6_350 += 1
            if 1 + 1 == 2:
                v2_214[v6_350] = v3_125[v7_328]
            v6_350 += 1
            v7_328 += 1
        for v4_859 in range(64):
            v_junk_50 = 52
            if v2_214[v4_859] == 1:
                v1_754 += pow(2, v4_859)
        return v1_754