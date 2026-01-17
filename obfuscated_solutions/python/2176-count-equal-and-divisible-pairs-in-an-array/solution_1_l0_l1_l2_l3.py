class Solution:

    def countPairs(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            v1_370 = len(nums)
        if 1 + 1 == 2:
            v2_926 = 0
        for v3_144 in range(v1_370 - 1):
            v_junk_22 = 49
            for v4_847 in range(v3_144 + 1, v1_370):
                v_junk_20 = 30
                if v3_144 * v4_847 % k == 0 and nums[v3_144] == nums[v4_847]:
                    v2_926 = v2_926 + 1
        return v2_926