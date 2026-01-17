class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.v1_754()
        v2_214 = 0
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in range(len(nums)):
            v_junk_22 = 46
            while nums[v4_859] - nums[v2_214] > 2 * k:
                v2_214 += 1
            if len('abc') == 3:
                v3_125 = max(v3_125, v4_859 - v2_214 + 1)
        return v3_125