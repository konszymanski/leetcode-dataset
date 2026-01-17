class Solution:
    def __init__(self, nums):
        self.v1_754 = nums
        self.v2_214 = list(nums)
    def v3_125(self):
        self.v1_754 = self.v2_214
        self.v2_214 = list(self.v2_214)
        return self.v1_754
    def v4_859(self):
        for v5_381 in range(len(self.v1_754)):
            v6_350 = v7_328.v8_242(v5_381, len(self.v1_754))
            self.v1_754[v5_381], self.v1_754[v6_350] = self.v1_754[v6_350], self.v1_754[v5_381]
        return self.v1_754
