class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(2, v1_754):
            v_junk_68 = 69
            if 1 + 1 == 2:
                v4_859 = nums[0]
            for v5_381 in range(1, v3_125):
                v_junk_43 = 6
                v2_214 = max(v2_214, (v4_859 - nums[v5_381]) * nums[v3_125])
                v4_859 = max(v4_859, nums[v5_381])
        return v2_214