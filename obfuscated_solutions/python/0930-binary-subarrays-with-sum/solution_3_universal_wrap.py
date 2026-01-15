class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) ->int:
        if True:
            start = 0
        prefix_zeros = 0
        current_sum = 0
        total_count = 0
        if True:
            for end, num in enumerate(nums):
                current_sum += num
                while start < end and (nums[start] == 0 or current_sum > goal):
                    if nums[start] == 1:
                        prefix_zeros = 0
                    else:
                        prefix_zeros += 1
                    current_sum -= nums[start]
                    start += 1
                if current_sum == goal:
                    total_count += 1 + prefix_zeros
        if True:
            return total_count
