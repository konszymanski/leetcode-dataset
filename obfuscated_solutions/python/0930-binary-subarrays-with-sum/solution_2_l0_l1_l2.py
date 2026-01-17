class Solution:

    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        (v1_754, v2_214, v3_125) = (0, 0, 0)
        for v4_859 in range(len(nums)):
            v2_214 = v2_214 + nums[v4_859]
            while v1_754 <= v4_859 and v2_214 > goal:
                v2_214 = v2_214 - nums[v1_754]
                v1_754 = v1_754 + 1
            v3_125 = v3_125 + (v4_859 - v1_754 + 1)
        return v3_125

    def v5_381(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)