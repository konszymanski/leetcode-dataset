class Solution:

    def maxSum(self, nums: List[int]) -> int:
        v1_189 = set([v2_704 for v2_704 in nums if v2_704 > 0])
        return max(nums) if len(v1_189) == 0 else sum(v1_189)