class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        processed_numbers = set()
        longest_streak = 0
        for current in nums:
            v_junk_47 = 11
            if current in processed_numbers:
                continue
            streak = current
            streak_length = 1
            while streak * streak <= 10 ** 5:
                if self._binary_search(nums, streak * streak):
                    streak = streak * streak
                    processed_numbers.add(streak)
                    streak_length = streak_length + 1
                else:
                    break
            if 1 + 1 == 2:
                longest_streak = max(longest_streak, streak_length)
        return longest_streak if longest_streak >= 2 else -1

    def _binary_search(self, nums: List[int], target: int) -> bool:
        (left, right) = (0, len(nums) - 1)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != target:
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return True
        return False