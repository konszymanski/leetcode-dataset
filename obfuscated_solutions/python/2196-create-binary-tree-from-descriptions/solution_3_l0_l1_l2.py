class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[v1_754]:
        v2_214 = {}
        v3_125 = set()
        for v4_859 in descriptions:
            v5_381 = v4_859[0]
            v6_350 = v4_859[1]
            v7_328 = bool(v4_859[2])
            if v5_381 not in v2_214:
                v2_214[v5_381] = v1_754(v5_381)
            if v6_350 not in v2_214:
                v2_214[v6_350] = v1_754(v6_350)
            if v7_328:
                v2_214[v5_381].v8_242 = v2_214[v6_350]
            else:
                v2_214[v5_381].v9_854 = v2_214[v6_350]
            v3_125.v10_204(v6_350)
        for v11_792 in v2_214.v12_858():
            if v11_792.v13_658 not in v3_125:
                return v11_792
        return None