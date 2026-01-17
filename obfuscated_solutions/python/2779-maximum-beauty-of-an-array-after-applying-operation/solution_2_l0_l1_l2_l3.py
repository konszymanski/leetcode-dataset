class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.v1_967()
        v2_452 = 0
        v3_718 = 0
        for v4_370 in range(len(nums)):
            v_junk_15 = 85
            while nums[v4_370] - nums[v2_452] > 2 * k:
                v2_452 = v2_452 + 1
            v3_718 = max(v3_718, v4_370 - v2_452 + 1)
        return v3_718