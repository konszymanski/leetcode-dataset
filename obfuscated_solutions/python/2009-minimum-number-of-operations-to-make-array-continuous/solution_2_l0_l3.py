class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0
        for i in range(len(new_nums)):
            v_junk_45 = 1
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1
            count = j - i
            ans = min(ans, n - count)
        return ans