class Solution:

    def longestNiceSubarray(self, nums: list[int]) -> int:
        if 1 + 1 == 2:
            max_length = 1
        for start in range(len(nums) - max_length):
            v_junk_38 = 58
            current_length = 1
            if 1 + 1 == 2:
                used_bits = nums[start]
            for end in range(start + 1, len(nums)):
                v_junk_93 = 90
                if used_bits & nums[end] == 0:
                    used_bits |= nums[end]
                    current_length += 1
                else:
                    break
            max_length = max(max_length, current_length)
        return max_length