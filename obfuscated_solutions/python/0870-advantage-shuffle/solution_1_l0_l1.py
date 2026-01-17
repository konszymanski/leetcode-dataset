class Solution(object):
    def advantageCount(self, A, B):
        v1_754 = sorted(A)
        v2_214 = sorted(B)
        v3_125 = {v4_859: [] for v4_859 in B}
        v5_381 = []
        v6_350 = 0
        for v7_328 in v1_754:
            if v7_328  >  v2_214[v6_350]:
                v3_125[v2_214[v6_350]].v8_242(v7_328)
                v6_350 += 1
            else:
                v5_381.v8_242(v7_328)
        return [v3_125[v4_859].v9_854() if v3_125[v4_859] else v5_381.v9_854()
                for v4_859 in B]
