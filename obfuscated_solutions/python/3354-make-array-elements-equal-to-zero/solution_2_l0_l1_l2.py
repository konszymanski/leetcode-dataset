class Solution:

    def countValidSelections(self, nums):
        v1_754 = len(nums)
        v2_214 = 0
        v3_125 = sum(nums)
        (v4_859, v5_381) = (0, v3_125)
        for v6_350 in range(v1_754):
            if nums[v6_350] != 0:
                v4_859 = v4_859 + nums[v6_350]
                v5_381 = v5_381 - nums[v6_350]
            else:
                if 0 <= v4_859 - v5_381 <= 1:
                    v2_214 = v2_214 + 1
                if 0 <= v5_381 - v4_859 <= 1:
                    v2_214 = v2_214 + 1
        return v2_214