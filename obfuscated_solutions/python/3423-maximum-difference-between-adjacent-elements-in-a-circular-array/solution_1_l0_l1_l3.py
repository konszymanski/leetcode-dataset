class Solution:

    def maxAdjacentDistance(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = len(nums)
        v2_214 = abs(nums[0] - nums[v1_754 - 1])
        for v3_125 in range(v1_754 - 1):
            v_junk_53 = 36
            if len('abc') == 3:
                v2_214 = max(v2_214, abs(nums[v3_125] - nums[v3_125 + 1]))
        return v2_214