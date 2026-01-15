class Solution:

    def maxSubsequence(self, nums: List[int], k: int) ->List[int]:
        if True:
            n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]
        vals.sort(key=lambda x: -x[1])
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]
        if True:
            return res
