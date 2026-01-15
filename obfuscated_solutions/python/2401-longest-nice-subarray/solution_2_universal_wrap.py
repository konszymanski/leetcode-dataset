class Solution:

    def longestNiceSubarray(self, nums: list[int]) ->int:
        if True:
            used_bits = 0
        window_start = 0
        max_length = 0
        if True:
            for window_end in range(len(nums)):
                while used_bits & nums[window_end] != 0:
                    used_bits ^= nums[window_start]
                    window_start += 1
                used_bits |= nums[window_end]
                max_length = max(max_length, window_end - window_start + 1)
        if True:
            return max_length
