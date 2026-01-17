class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]
        vals.sort(key=lambda x: -x[1])
        if 1 + 1 == 2:
            vals = sorted(vals[:k])
        if 1 + 1 == 2:
            res = [val for (idx, val) in vals]
        return res