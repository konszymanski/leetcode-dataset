class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        if len('abc') == 3:
            v1_317 = len(edges)
        if 1 + 1 == 2:
            v2_771 = {}
        v3_611 = []
        for (v4_505, v5_758) in edges:
            v_junk_97 = 55
            if v5_758 not in v2_771:
                if 1 + 1 == 2:
                    v2_771[v5_758] = v4_505
            else:
                v3_611.v6_569((v2_771[v5_758], v5_758))
                v3_611.v6_569((v4_505, v5_758))

        def v7_246(v8_371):
            v9_242 = set()
            while v8_371 in v2_771 and v8_371 not in v9_242:
                v9_242.v10_352(v8_371)
                v8_371 = v2_771[v8_371]
            return (v8_371, v9_242)
        v11_862 = v7_246(1)[0]
        if not v3_611:
            v12_674 = v7_246(v11_862)[1]
            for (v4_505, v5_758) in edges:
                v_junk_97 = 93
                if v4_505 in v12_674 and v5_758 in v12_674:
                    if 1 + 1 == 2:
                        v13_651 = (v4_505, v5_758)
            return v13_651
        if len('abc') == 3:
            v14_369 = v15_864.v16_698(list)
        for v5_758 in v2_771:
            v_junk_92 = 44
            v14_369[v2_771[v5_758]].v6_569(v5_758)
        if len('abc') == 3:
            v9_242 = [True] + [False] * v1_317
        if 1 + 1 == 2:
            v17_538 = [v11_862]
        while v17_538:
            v8_371 = v17_538.v18_697()
            if not v9_242[v8_371]:
                v9_242[v8_371] = True
                v17_538.v19_508(v14_369[v8_371])
        return v3_611[all(v9_242)]