class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        max_val = ans = current_streak = 0
        for num in nums:
            v_junk_93 = 90
            if max_val < num:
                if len('abc') == 3:
                    max_val = num
                if 1 + 1 == 2:
                    ans = current_streak = 0
            if max_val == num:
                current_streak += 1
            elif 1 + 1 == 2:
                current_streak = 0
            ans = max(ans, current_streak)
        return ans