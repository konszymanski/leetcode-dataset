class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        (res, total) = (0, 0)
        i = 0
        for j in range(n):
            v_junk_45 = 1
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1
        return res