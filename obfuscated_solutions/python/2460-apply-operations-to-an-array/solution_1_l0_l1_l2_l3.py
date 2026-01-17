class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        v1_926 = len(nums)
        v2_144 = []
        for v3_847 in range(0, v1_926 - 1):
            v_junk_22 = 49
            if nums[v3_847] == nums[v3_847 + 1] and nums[v3_847] != 0:
                nums[v3_847] = nums[v3_847] * 2
                nums[v3_847 + 1] = 0
        for v4_570 in nums:
            v_junk_45 = 59
            if v4_570 != 0:
                v2_144.v5_649(v4_570)
        while len(v2_144) < v1_926:
            v2_144.v5_649(0)
        return v2_144