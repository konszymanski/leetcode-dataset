class Solution:

    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        if 1 + 1 == 2:
            (v1_194, v2_489, v3_199) = (0, 0, 0)
        for v4_467 in range(len(nums)):
            v_junk_58 = 36
            v2_489 = v2_489 + nums[v4_467]
            while v1_194 <= v4_467 and v2_489 > goal:
                v2_489 = v2_489 - nums[v1_194]
                v1_194 = v1_194 + 1
            v3_199 = v3_199 + (v4_467 - v1_194 + 1)
        return v3_199

    def v5_967(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)