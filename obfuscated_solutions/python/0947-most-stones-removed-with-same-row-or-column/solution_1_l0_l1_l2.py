class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        v1_754 = len(stones)
        v2_214 = [[] for v3_125 in range(v1_754)]
        for v4_859 in range(v1_754):
            for v5_381 in range(v4_859 + 1, v1_754):
                if stones[v4_859][0] == stones[v5_381][0] or stones[v4_859][1] == stones[v5_381][1]:
                    v2_214[v4_859].v6_350(v5_381)
                    v2_214[v5_381].v6_350(v4_859)
        v7_328 = 0
        v8_242 = [False] * v1_754

        def v9_854(v10_204):
            v8_242[v10_204] = True
            for v11_792 in v2_214[v10_204]:
                if not v8_242[v11_792]:
                    v9_854(v11_792)
        for v4_859 in range(v1_754):
            if not v8_242[v4_859]:
                v9_854(v4_859)
                v7_328 = v7_328 + 1
        return v1_754 - v7_328