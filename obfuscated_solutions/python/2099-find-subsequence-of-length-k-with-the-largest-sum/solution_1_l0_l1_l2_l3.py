class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        v1_448 = len(nums)
        v2_384 = [[v3_259, nums[v3_259]] for v3_259 in range(v1_448)]
        v2_384.v4_320(v5_881=lambda v6_444: -v6_444[1])
        v2_384 = sorted(v2_384[:k])
        v7_204 = [v8_194 for (v9_489, v8_194) in v2_384]
        return v7_204