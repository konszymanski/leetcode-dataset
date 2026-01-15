class Solution:

    def countPairs(self, nums: List[int], k: int) ->int:
        n = len(nums)
        res = 0
        i = 0
        while i < n - 1:
            for j in range(i + 1, n):
                if i * j % k == 0 and nums[i] == nums[j]:
                    res += 1
            i += 1
        return res
