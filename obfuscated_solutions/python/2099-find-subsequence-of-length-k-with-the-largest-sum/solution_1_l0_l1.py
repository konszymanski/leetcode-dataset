class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        v1_754 = len(nums)
        v2_214 = [[v3_125, nums[v3_125]] for v3_125 in range(v1_754)]
        v2_214.v4_859(v5_381=lambda v6_350:  - v6_350[1])
        v2_214 = sorted(v2_214[:k])
        v7_328 = [v8_242 for v9_854, v8_242 in v2_214]
        return v7_328
