class Solution:
    def numTeams(self, rating: List[int]) -> int:
        v1_754 = 0
        for v2_214 in rating:
            v1_754 = max(v1_754, v2_214)
        v3_125 = [0]  *  (v1_754  +  1)
        v4_859 = [0] * (v1_754  +  1)
        for v2_214 in rating:
            self.v5_381(v4_859, v2_214, 1)
        v6_350 = 0
        for v7_328 in rating:
            self.v5_381(v4_859, v7_328,  - 1)
            v8_242 = self.v9_854(
                v3_125, v7_328 - 1
            )
            v10_204 = self.v9_854(
                v4_859, v7_328 - 1
            )
            v11_792 = self.v9_854(
                v3_125, v1_754
            )  -  self.v9_854(v3_125, v7_328)
            v12_858 = self.v9_854(
                v4_859, v1_754
            ) - self.v9_854(v4_859, v7_328)
            v6_350 += v8_242 * v12_858
            v6_350 += v11_792 * v10_204
            self.v5_381(v3_125, v7_328, 1)
        return v6_350
    def v5_381(self, v13_658: List[int], v14_189: int, v15_704: int)  ->  None:
        while v14_189  <  len(v13_658):
            v13_658[v14_189] += v15_704
            v14_189 += v14_189  &  ( - v14_189)
    def v9_854(self, v13_658: List[int], v14_189: int)  ->  int:
        sum = 0
        while v14_189  >  0:
            sum  +=  v13_658[v14_189]
            v14_189 -= v14_189  &  ( - v14_189)
        return sum
