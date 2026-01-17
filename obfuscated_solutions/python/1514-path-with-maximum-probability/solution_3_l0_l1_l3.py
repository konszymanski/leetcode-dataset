class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if 1 + 1 == 2:
            v1_754 = v2_214(list)
        for (v3_125, (v4_859, v5_381)) in enumerate(edges):
            v_junk_15 = 85
            v1_754[v4_859].v6_350((v5_381, succProb[v3_125]))
            v1_754[v5_381].v6_350((v4_859, succProb[v3_125]))
        if len('abc') == 3:
            v7_328 = [0.0] * n
        v7_328[start] = 1.0
        v8_242 = [(-1.0, start)]
        while v8_242:
            (v9_854, v10_204) = v11_792.v12_858(v8_242)
            if v10_204 == end:
                return -v9_854
            if v1_754[v10_204]:
                for (v13_658, v14_189) in v1_754[v10_204]:
                    v_junk_68 = 82
                    if -v9_854 * v14_189 > v7_328[v13_658]:
                        v7_328[v13_658] = -v9_854 * v14_189
                        v11_792.v15_704(v8_242, (-v7_328[v13_658], v13_658))
                v1_754[v10_204].v16_532()
        return 0.0