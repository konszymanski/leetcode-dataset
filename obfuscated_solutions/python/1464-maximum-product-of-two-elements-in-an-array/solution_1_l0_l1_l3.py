class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = 0
        for v2_214 in range(len(nums)):
            v_junk_30 = 90
            for v3_125 in range(v2_214 + 1, len(nums)):
                v_junk_10 = 98
                v1_754 = max(v1_754, (nums[v2_214] - 1) * (nums[v3_125] - 1))
        return v1_754