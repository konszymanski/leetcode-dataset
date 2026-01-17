class Solution(object):

    def loudAndRich(self, richer, quiet):
        v1_754 = len(quiet)
        v2_214 = [[] for v3_125 in v4_859(v1_754)]
        for (v5_381, v6_350) in richer:
            v2_214[v6_350].v7_328(v5_381)
        v8_242 = [None] * v1_754

        def v9_854(v10_204):
            if v8_242[v10_204] is None:
                v8_242[v10_204] = v10_204
                for v11_792 in v2_214[v10_204]:
                    v12_858 = v9_854(v11_792)
                    if quiet[v12_858] < quiet[v8_242[v10_204]]:
                        v8_242[v10_204] = v12_858
            return v8_242[v10_204]
        return map(v9_854, range(v1_754))