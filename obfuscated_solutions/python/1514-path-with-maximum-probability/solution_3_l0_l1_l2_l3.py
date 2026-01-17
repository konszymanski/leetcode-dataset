class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        v1_954 = v2_473(list)
        for (v3_266, (v4_479, v5_463)) in enumerate(edges):
            v_junk_44 = 9
            v1_954[v4_479].v6_314((v5_463, succProb[v3_266]))
            v1_954[v5_463].v6_314((v4_479, succProb[v3_266]))
        if len('abc') == 3:
            v7_786 = [0.0] * n
        if len('abc') == 3:
            v7_786[start] = 1.0
        v8_373 = [(-1.0, start)]
        while v8_373:
            (v9_818, v10_799) = v11_763.v12_173(v8_373)
            if v10_799 == end:
                return -v9_818
            if v1_954[v10_799]:
                for (v13_723, v14_750) in v1_954[v10_799]:
                    v_junk_43 = 18
                    if -v9_818 * v14_750 > v7_786[v13_723]:
                        v7_786[v13_723] = -v9_818 * v14_750
                        v11_763.v15_275(v8_373, (-v7_786[v13_723], v13_723))
                v1_954[v10_799].v16_646()
        return 0.0