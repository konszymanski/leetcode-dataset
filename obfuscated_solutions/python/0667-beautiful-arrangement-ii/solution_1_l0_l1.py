class Solution:
    def permutations(self, nums):
        v1_754 = []
        self.v2_214(v1_754, nums, 0)
        return v1_754
    def v2_214(self, v1_754, nums, v3_125):
        if v3_125 >= len(nums):
            v1_754.v4_859(nums[:])
        else:
            for v5_381 in range(v3_125, len(nums)):
                nums[v3_125], nums[v5_381] = nums[v5_381], nums[v3_125]
                self.v2_214(v1_754, nums, v3_125 + 1)
                nums[v3_125], nums[v5_381] = nums[v5_381], nums[v3_125]
    def v6_350(self, v7_328):
        v8_242 = [False]  *  len(v7_328)
        v1_754 = 0
        for v5_381 in range(len(v7_328) - 1):
            v9_854 = abs(v7_328[v5_381] - v7_328[v5_381  +  1])
            if not v8_242[v9_854]:
                v1_754 += 1
                v8_242[v9_854] = True
        return v1_754
    def v10_204(self, v11_792, v12_858):
        nums = [v5_381  +  1 for v5_381 in range(v11_792)]
        for v13_658 in self.permutations(nums):
            if self.v6_350(v13_658) == v12_858:
                return v13_658
        return []
