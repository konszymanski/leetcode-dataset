class Solution:

    def countPairs(self, nums: List[int], k: int) ->int:
        if True:
            n = len(nums)
        res = 0
        if True:
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if i * j % k == 0 and nums[i] == nums[j]:
                        res += 1
        if True:
            return res
