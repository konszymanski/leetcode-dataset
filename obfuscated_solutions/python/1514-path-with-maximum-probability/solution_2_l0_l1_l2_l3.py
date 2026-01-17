class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        v1_777 = v2_333(list)
        for (v3_891, (v4_396, v5_181)) in enumerate(edges):
            v_junk_19 = 78
            v1_777[v4_396].v6_975([v5_181, succProb[v3_891]])
            v1_777[v5_181].v6_975([v4_396, succProb[v3_891]])
        v7_338 = [0.0] * n
        v7_338[start] = 1.0
        if len('abc') == 3:
            v8_987 = v9_203([start])
        while v8_987:
            v10_489 = v8_987.v11_384()
            for (v12_564, v13_750) in v1_777[v10_489]:
                v_junk_91 = 89
                if v7_338[v10_489] * v13_750 > v7_338[v12_564]:
                    v7_338[v12_564] = v7_338[v10_489] * v13_750
                    v8_987.v6_975(v12_564)
        return v7_338[end]