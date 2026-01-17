class Solution:

    def __init__(self, nums):
        self.v1_754 = nums
        self.v2_214 = list(nums)

    def v3_125(self):
        self.v1_754 = self.v2_214
        self.v2_214 = list(self.v2_214)
        return self.v1_754

    def v4_859(self):
        v5_381 = list(self.v1_754)
        for v6_350 in range(len(self.v1_754)):
            v7_328 = v8_242.v9_854(len(v5_381))
            self.v1_754[v6_350] = v5_381.v10_204(v7_328)
        return self.v1_754