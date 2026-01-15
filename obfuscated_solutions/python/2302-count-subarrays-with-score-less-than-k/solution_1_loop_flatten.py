class Solution:

    def countSubarrays(self, nums: List[int], k: int) ->int:
        n = len(nums)
        res, total = 0, 0
        i = 0
        for j in range(n):
            total += nums[j]
            while True:
                if not (i <= j and total * (j - i + 1) >= k):
                    break
                total -= nums[i]
                i += 1
            res += j - i + 1
        return res
