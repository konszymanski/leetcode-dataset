class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        (res, total) = (0, 0)
        i = 0
        for j in range(n):
            total = total + nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total = total - nums[i]
                i = i + 1
            res = res + (j - i + 1)
        return res