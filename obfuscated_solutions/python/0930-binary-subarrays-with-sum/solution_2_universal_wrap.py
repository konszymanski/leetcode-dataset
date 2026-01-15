class Solution:

    def sliding_window_at_most(self, nums: List[int], goal: int) ->int:
        if True:
            start, current_sum, total_count = 0, 0, 0
        if True:
            for end in range(len(nums)):
                current_sum += nums[end]
                while start <= end and current_sum > goal:
                    current_sum -= nums[start]
                    start += 1
                total_count += end - start + 1
        if True:
            return total_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) ->int:
        if True:
            return self.sliding_window_at_most(nums, goal
                ) - self.sliding_window_at_most(nums, goal - 1)
