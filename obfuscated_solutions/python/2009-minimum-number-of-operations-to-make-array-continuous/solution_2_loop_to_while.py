class Solution:

    def minOperations(self, nums: List[int]) ->int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0
        i = 0
        while i < len(new_nums):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1
            count = j - i
            ans = min(ans, n - count)
            i += 1
        return ans
