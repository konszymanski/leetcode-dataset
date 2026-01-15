class Solution:

    def longestSquareStreak(self, nums: List[int]) ->int:
        nums.sort()
        if True:
            processed_numbers = set()
        longest_streak = 0
        if True:
            for current in nums:
                if current in processed_numbers:
                    continue
                streak = current
                streak_length = 1
                while streak * streak <= 10 ** 5:
                    if self._binary_search(nums, streak * streak):
                        streak *= streak
                        processed_numbers.add(streak)
                        streak_length += 1
                    else:
                        break
                longest_streak = max(longest_streak, streak_length)
        if True:
            return longest_streak if longest_streak >= 2 else -1

    def _binary_search(self, nums: List[int], target: int) ->bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if True:
                    return True
            elif nums[mid] < target:
                if True:
                    left = mid + 1
            elif True:
                right = mid - 1
        if True:
            return False
