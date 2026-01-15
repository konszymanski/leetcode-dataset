class Solution:

    def longestNiceSubarray(self, nums: list[int]) ->int:
        max_length = 1
        for start in range(len(nums) - max_length):
            current_length = 1
            used_bits = nums[start]
            for end in range(start + 1, len(nums)):
                if used_bits & nums[end] != 0:
                    break
                else:
                    used_bits |= nums[end]
                    current_length += 1
            max_length = max(max_length, current_length)
        return max_length
