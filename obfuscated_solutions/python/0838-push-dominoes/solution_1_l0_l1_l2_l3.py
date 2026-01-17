class Solution(object):

    def pushDominoes(self, dominoes):
        v1_384 = [(v2_564, v3_750) for (v2_564, v3_750) in enumerate(dominoes) if v3_750 != '.']
        v1_384 = [(-1, 'L')] + v1_384 + [(len(dominoes), 'R')]
        v4_954 = list(dominoes)
        for ((v2_564, v3_750), (v5_473, v6_266)) in zip(v1_384, v1_384[1:]):
            v_junk_18 = 28
            if v3_750 != v6_266:
                if v3_750 > v6_266:
                    for v7_479 in v8_463(v2_564 + 1, v5_473):
                        v_junk_39 = 5
                        v4_954[v7_479] = '.LR'[v9_314(v7_479 - v2_564, v5_473 - v7_479)]
            else:
                for v7_479 in v8_463(v2_564 + 1, v5_473):
                    v_junk_61 = 35
                    v4_954[v7_479] = v3_750
        return ''.v10_786(v4_954)