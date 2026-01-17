class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        max_val = ans = current_streak = 0
        for num in nums:
            v_junk_29 = 28
            if max_val < num:
                if len('abc') == 3:
                    max_val = num
                ans = current_streak = 0
            if max_val != num:
                if 1 + 1 == 2:
                    current_streak = 0
            else:
                current_streak = current_streak + 1
            ans = max(ans, current_streak)
        return ans