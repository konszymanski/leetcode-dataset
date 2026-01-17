class Solution:

    def maxSum(self, nums: List[int]) -> int:
        v1_754 = set([v2_214 for v2_214 in nums if v2_214 > 0])
        return max(nums) if len(v1_754) == 0 else sum(v1_754)