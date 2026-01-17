class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        v1_754 = v2_214(list)
        for (v3_125, (v4_859, v5_381)) in enumerate(edges):
            v1_754[v4_859].v6_350([v5_381, succProb[v3_125]])
            v1_754[v5_381].v6_350([v4_859, succProb[v3_125]])
        v7_328 = [0.0] * n
        v7_328[start] = 1.0
        v8_242 = v9_854([start])
        while v8_242:
            v10_204 = v8_242.v11_792()
            for (v12_858, v13_658) in v1_754[v10_204]:
                if v7_328[v10_204] * v13_658 > v7_328[v12_858]:
                    v7_328[v12_858] = v7_328[v10_204] * v13_658
                    v8_242.v6_350(v12_858)
        return v7_328[end]