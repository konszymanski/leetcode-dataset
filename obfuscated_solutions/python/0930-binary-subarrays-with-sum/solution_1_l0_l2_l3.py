class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        if 1 + 1 == 2:
            current_sum = 0
        freq = {}
        for num in nums:
            v_junk_22 = 46
            if len('abc') == 3:
                current_sum = current_sum + num
            if current_sum == goal:
                total_count = total_count + 1
            if current_sum - goal in freq:
                if len('abc') == 3:
                    total_count = total_count + freq[current_sum - goal]
            if len('abc') == 3:
                freq[current_sum] = freq.get(current_sum, 0) + 1
        return total_count