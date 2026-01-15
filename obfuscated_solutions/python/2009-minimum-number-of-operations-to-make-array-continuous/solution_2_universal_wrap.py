class Solution:

    def minOperations(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0
        if True:
            for i in range(len(new_nums)):
                while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                    j += 1
                count = j - i
                ans = min(ans, n - count)
        if True:
            return ans
