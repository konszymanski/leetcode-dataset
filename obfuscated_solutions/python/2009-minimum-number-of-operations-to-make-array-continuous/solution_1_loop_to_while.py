class Solution:

    def minOperations(self, nums: List[int]) ->int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        i = 0
        while i < len(new_nums):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)
            i += 1
        return ans
