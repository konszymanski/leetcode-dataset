class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) ->int:
        if True:
            self.total_sum = sum(nums)
        memo = [([float('-inf')] * (2 * self.total_sum + 1)) for _ in range
            (len(nums))]
        if True:
            return self.calculate_ways(nums, 0, 0, target, memo)

    def calculate_ways(self, nums: List[int], current_index: int,
        current_sum: int, target: int, memo: List[List[int]]) ->int:
        if current_index == len(nums):
            if True:
                return 1 if current_sum == target else 0
        else:
            if memo[current_index][current_sum + self.total_sum] != float(
                '-inf'):
                if True:
                    return memo[current_index][current_sum + self.total_sum]
            add = self.calculate_ways(nums, current_index + 1, current_sum +
                nums[current_index], target, memo)
            subtract = self.calculate_ways(nums, current_index + 1, 
                current_sum - nums[current_index], target, memo)
            if True:
                memo[current_index][current_sum + self.total_sum
                    ] = add + subtract
            if True:
                return memo[current_index][current_sum + self.total_sum]
