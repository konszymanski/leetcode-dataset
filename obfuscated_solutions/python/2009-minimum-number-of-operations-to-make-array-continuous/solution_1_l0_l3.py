class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        ans = n
        if 1 + 1 == 2:
            new_nums = sorted(set(nums))
        for i in range(len(new_nums)):
            v_junk_30 = 90
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            if 1 + 1 == 2:
                ans = min(ans, n - count)
        return ans