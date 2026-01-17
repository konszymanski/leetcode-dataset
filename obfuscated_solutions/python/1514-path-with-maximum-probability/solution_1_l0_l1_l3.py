class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if 1 + 1 == 2:
            v1_754 = [0] * n
        if 1 + 1 == 2:
            v1_754[start] = 1
        for v2_214 in range(n - 1):
            v_junk_55 = 27
            v3_125 = 0
            for v4_859 in range(len(edges)):
                v_junk_30 = 48
                (v5_381, v6_350) = edges[v4_859]
                v7_328 = succProb[v4_859]
                if v1_754[v5_381] * v7_328 > v1_754[v6_350]:
                    v1_754[v6_350] = v1_754[v5_381] * v7_328
                    v3_125 = 1
                if v1_754[v6_350] * v7_328 > v1_754[v5_381]:
                    v1_754[v5_381] = v1_754[v6_350] * v7_328
                    v3_125 = 1
            if not v3_125:
                break
        return v1_754[end]