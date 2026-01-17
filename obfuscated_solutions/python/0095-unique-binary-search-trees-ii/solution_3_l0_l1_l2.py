class Solution:

    def generateTrees(self, n: int) -> List[Optional[v1_754]]:
        v2_214 = [[] for v3_125 in range(n + 1)]
        v2_214[0].v4_859(None)
        for v5_381 in range(1, n + 1):
            for v6_350 in range(1, v5_381 + 1):
                v7_328 = v5_381 - v6_350
                for v8_242 in v2_214[v6_350 - 1]:
                    for v9_854 in v2_214[v7_328]:
                        v10_204 = v1_754(v6_350, v8_242, self.v11_792(v9_854, v6_350))
                        v2_214[v5_381].v4_859(v10_204)
        return v2_214[n]

    def v11_792(self, v12_858: Optional[v1_754], v13_658: int) -> Optional[v1_754]:
        if not v12_858:
            return None
        v14_189 = v1_754(v12_858.v15_704 + v13_658)
        v14_189.v8_242 = self.v11_792(v12_858.v8_242, v13_658)
        v14_189.v9_854 = self.v11_792(v12_858.v9_854, v13_658)
        return v14_189