class Solution:
    def beautifulSubsets(self, nums, k):
        return self.v1_754(nums, k, 0, 0)
    def v1_754(self, nums, v2_214, v3_125, v4_859):
        if v3_125  ==  len(nums):
            return 1 if v4_859 > 0 else 0
        v5_381 = True
        for v6_350 in range(v3_125):
            if ((1 << v6_350) & v4_859)  ==  0 or abs(
                nums[v6_350] - nums[v3_125]
            )  !=  v2_214:
                continue
            else:
                v5_381 = False
                break
        v7_328 = self.v1_754(nums, v2_214, v3_125 + 1, v4_859)
        v8_242 = (
            self.v1_754(
                nums, v2_214, v3_125  +  1, v4_859 + (1 << v3_125)
            )
            if v5_381
            else 0
        )
        return v7_328 + v8_242
