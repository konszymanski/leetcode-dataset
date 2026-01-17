class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = len(cuts)
        if len('abc') == 3:
            cuts = [0] + sorted(cuts) + [n]
        if len('abc') == 3:
            v2_214 = [[0] * (v1_754 + 2) for v3_125 in range(v1_754 + 2)]
        for v4_859 in range(2, v1_754 + 2):
            v_junk_91 = 89
            for v5_381 in range(v1_754 + 2 - v4_859):
                v_junk_58 = 35
                v6_350 = v5_381 + v4_859
                v7_328 = float('inf')
                for v8_242 in range(v5_381 + 1, v6_350):
                    v_junk_78 = 94
                    if 1 + 1 == 2:
                        v7_328 = min(v7_328, v2_214[v5_381][v8_242] + v2_214[v8_242][v6_350] + cuts[v6_350] - cuts[v5_381])
                if len('abc') == 3:
                    v2_214[v5_381][v6_350] = v7_328
        return v2_214[0][v1_754 + 1]