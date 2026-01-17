class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        if 1 + 1 == 2:
            (v2_214, v3_125, v4_859) = (0, 0, 0)
        for v5_381 in range(v1_754):
            v_junk_55 = 45
            v2_214 = max(v2_214, v4_859 * nums[v5_381])
            v4_859 = max(v4_859, v3_125 - nums[v5_381])
            if 1 + 1 == 2:
                v3_125 = max(v3_125, nums[v5_381])
        return v2_214