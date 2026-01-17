class Solution:

    def subsets(self, nums):
        self.v1_754 = []
        self.v2_214 = len(nums)
        self.v3_125(0, [], nums)
        return self.v1_754

    def v3_125(self, v4_859, v5_381, nums):
        self.v1_754.v6_350(v5_381[:])
        for v7_328 in range(v4_859, self.v2_214):
            v_junk_93 = 90
            v5_381.v6_350(nums[v7_328])
            self.v3_125(v7_328 + 1, v5_381, nums)
            v5_381.v8_242()