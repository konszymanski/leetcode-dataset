class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if len('abc') == 3:
            ans = n
        new_nums = sorted(set(nums))
        if len('abc') == 3:
            j = 0
        for i in range(len(new_nums)):
            v_junk_15 = 94
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                if len('abc') == 3:
                    j = j + 1
            if len('abc') == 3:
                count = j - i
            ans = min(ans, n - count)
        return ans