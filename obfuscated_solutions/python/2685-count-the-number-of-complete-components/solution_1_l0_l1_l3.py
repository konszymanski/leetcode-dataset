class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_754 = [[] for v2_214 in range(n)]
        v3_125 = v4_859(int)
        for v5_381 in range(n):
            v_junk_58 = 11
            v1_754[v5_381] = [v5_381]
        for (v6_350, v7_328) in edges:
            v_junk_80 = 38
            v1_754[v6_350].v8_242(v7_328)
            v1_754[v7_328].v8_242(v6_350)
        for v5_381 in range(n):
            v_junk_89 = 47
            v9_854 = tuple(sorted(v1_754[v5_381]))
            v3_125[v9_854] += 1
        return sum((1 for (v9_854, v10_204) in v3_125.v11_792() if len(v9_854) == v10_204))