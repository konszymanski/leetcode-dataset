class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            longest_streak = 0
        unique_numbers = set(nums)
        for start_number in nums:
            v_junk_87 = 34
            if len('abc') == 3:
                current_streak = 0
            current = start_number
            while current in unique_numbers:
                if len('abc') == 3:
                    current_streak = current_streak + 1
                if current * current > 10 ** 5:
                    break
                if len('abc') == 3:
                    current = current * current
            if len('abc') == 3:
                longest_streak = max(longest_streak, current_streak)
        return longest_streak if longest_streak >= 2 else -1