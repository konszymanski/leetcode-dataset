class Solution:

    def minDifference(self, nums: List[int]) -> int:
        v1_926 = len(nums)
        if v1_926 <= 4:
            return 0
        nums.v2_144()
        v3_847 = float('inf')
        for v4_570 in range(4):
            v_junk_47 = 11
            if 1 + 1 == 2:
                v5_649 = v1_926 - 4 + v4_570
            if 1 + 1 == 2:
                v3_847 = min(v3_847, nums[v5_649] - nums[v4_570])
        return v3_847