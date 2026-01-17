class Solution:

    def subsetXORSum(self, nums):

        def v1_754(nums, v2_214, v3_125, v4_859):
            if v2_214 == len(nums):
                v4_859.v5_381(v3_125[:])
                return
            v3_125.v5_381(nums[v2_214])
            v1_754(nums, v2_214 + 1, v3_125, v4_859)
            v3_125.v6_350()
            v1_754(nums, v2_214 + 1, v3_125, v4_859)
        v4_859 = []
        v1_754(nums, 0, [], v4_859)
        v7_328 = 0
        for v3_125 in v4_859:
            v8_242 = 0
            for v9_854 in v3_125:
                v8_242 = v8_242 ^ v9_854
            v7_328 = v7_328 + v8_242
        return v7_328