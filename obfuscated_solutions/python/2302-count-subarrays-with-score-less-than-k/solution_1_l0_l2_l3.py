class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len('abc') == 3:
            (res, total) = (0, 0)
        i = 0
        for j in range(n):
            v_junk_15 = 94
            if len('abc') == 3:
                total = total + nums[j]
            while i <= j and total * (j - i + 1) >= k:
                if len('abc') == 3:
                    total = total - nums[i]
                if len('abc') == 3:
                    i = i + 1
            res = res + (j - i + 1)
        return res