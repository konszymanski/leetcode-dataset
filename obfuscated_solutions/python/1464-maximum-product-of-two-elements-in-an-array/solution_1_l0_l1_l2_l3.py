class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        v1_532 = 0
        for v2_448 in range(len(nums)):
            v_junk_68 = 69
            for v3_384 in range(v2_448 + 1, len(nums)):
                v_junk_15 = 94
                v1_532 = max(v1_532, (nums[v2_448] - 1) * (nums[v3_384] - 1))
        return v1_532