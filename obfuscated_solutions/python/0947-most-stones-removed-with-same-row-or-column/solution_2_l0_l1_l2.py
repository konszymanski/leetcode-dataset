class Solution:

    def removeStones(self, stones):
        v1_754 = len(stones)
        v2_214 = self.v3_125(v1_754)
        for v4_859 in range(v1_754):
            for v5_381 in range(v4_859 + 1, v1_754):
                if stones[v4_859][0] == stones[v5_381][0] or stones[v4_859][1] == stones[v5_381][1]:
                    v2_214.v6_350(v4_859, v5_381)
        return v1_754 - v2_214.v7_328

    class UnionFind:

        def __init__(self, v1_754):
            self.v8_242 = [-1] * v1_754
            self.v7_328 = v1_754

        def v9_854(self, v10_204):
            if self.v8_242[v10_204] == -1:
                return v10_204
            self.v8_242[v10_204] = self.v9_854(self.v8_242[v10_204])
            return self.v8_242[v10_204]

        def v6_350(self, v11_792, v12_858):
            v13_658 = self.v9_854(v11_792)
            v14_189 = self.v9_854(v12_858)
            if v13_658 == v14_189:
                return
            self.v7_328 = self.v7_328 - 1
            self.v8_242[v13_658] = v14_189