class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        (v1_754, v2_214) = (0, -1)
        v3_125 = v4_859()
        for v5_381 in range(len(nums)):
            v3_125[nums[v5_381]] = v3_125[nums[v5_381]] + 1
            while v3_125[nums[v5_381]] > k:
                v2_214 = v2_214 + 1
                v3_125[nums[v2_214]] = v3_125[nums[v2_214]] - 1
            v1_754 = max(v1_754, v5_381 - v2_214)
        return v1_754