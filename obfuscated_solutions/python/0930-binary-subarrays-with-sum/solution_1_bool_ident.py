class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) ->int:
        total_count = 0
        current_sum = 0
        freq = {}
        for num in nums:
            current_sum += num
            if current_sum == goal and 1 + 1 == 2:
                total_count += 1
            if current_sum - goal in freq and 1 + 1 == 2:
                total_count += freq[current_sum - goal]
            freq[current_sum] = freq.get(current_sum, 0) + 1
        return total_count
