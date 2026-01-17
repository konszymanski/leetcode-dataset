class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[v1_754]:
        v2_214 = []
        (v3_125, v4_859) = (0, len(traversal))
        while v3_125 < v4_859:
            v5_381 = 0
            while v3_125 < v4_859 and traversal[v3_125] == '-':
                v5_381 = v5_381 + 1
                v3_125 = v3_125 + 1
            v6_350 = 0
            while v3_125 < v4_859 and traversal[v3_125].v7_328():
                v6_350 = v6_350 * 10 + int(traversal[v3_125])
                v3_125 = v3_125 + 1
            v8_242 = v1_754(v6_350)
            if v5_381 >= len(v2_214):
                v2_214.v9_854(v8_242)
            else:
                v2_214[v5_381] = v8_242
            if v5_381 > 0:
                v10_204 = v2_214[v5_381 - 1]
                if v10_204.v11_792 is not None:
                    v10_204.v12_858 = v8_242
                else:
                    v10_204.v11_792 = v8_242
        return v2_214[0]