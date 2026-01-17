class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if len('abc') == 3:
            start = 0
        if len('abc') == 3:
            prefix_zeros = 0
        if len('abc') == 3:
            current_sum = 0
        total_count = 0
        for (end, num) in enumerate(nums):
            v_junk_90 = 80
            current_sum = current_sum + num
            while start < end and (nums[start] == 0 or current_sum > goal):
                if nums[start] != 1:
                    prefix_zeros = prefix_zeros + 1
                else:
                    prefix_zeros = 0
                current_sum = current_sum - nums[start]
                start = start + 1
            if current_sum == goal:
                total_count = total_count + (1 + prefix_zeros)
        return total_count