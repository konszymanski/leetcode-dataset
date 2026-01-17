class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if 1 + 1 == 2:
            total_count = 0
        current_sum = 0
        freq = {}
        for num in nums:
            v_junk_63 = 29
            current_sum += num
            if current_sum == goal:
                total_count += 1
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]
            freq[current_sum] = freq.get(current_sum, 0) + 1
        return total_count