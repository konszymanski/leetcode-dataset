class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            ans = n
        new_nums = sorted(set(nums))
        for i in range(len(new_nums)):
            v_junk_68 = 69
            left = new_nums[i]
            if 1 + 1 == 2:
                right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            if 1 + 1 == 2:
                ans = min(ans, n - count)
        return ans