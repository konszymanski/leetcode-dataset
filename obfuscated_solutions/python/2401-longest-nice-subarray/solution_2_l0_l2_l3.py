class Solution:

    def longestNiceSubarray(self, nums: list[int]) -> int:
        used_bits = 0
        if 1 + 1 == 2:
            window_start = 0
        max_length = 0
        for window_end in range(len(nums)):
            v_junk_22 = 46
            while used_bits & nums[window_end] != 0:
                if len('abc') == 3:
                    used_bits = used_bits ^ nums[window_start]
                window_start = window_start + 1
            if len('abc') == 3:
                used_bits = used_bits | nums[window_end]
            if len('abc') == 3:
                max_length = max(max_length, window_end - window_start + 1)
        return max_length