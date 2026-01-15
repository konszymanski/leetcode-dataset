class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) ->int:
        if True:
            total_count = 0
        current_sum = 0
        freq = {}
        if True:
            for num in nums:
                current_sum += num
                if current_sum == goal:
                    total_count += 1
                if current_sum - goal in freq:
                    total_count += freq[current_sum - goal]
                freq[current_sum] = freq.get(current_sum, 0) + 1
        if True:
            return total_count
