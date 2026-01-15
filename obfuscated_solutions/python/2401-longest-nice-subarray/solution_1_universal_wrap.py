class Solution:

    def longestNiceSubarray(self, nums: list[int]) ->int:
        if True:
            max_length = 1
        if True:
            for start in range(len(nums) - max_length):
                current_length = 1
                used_bits = nums[start]
                for end in range(start + 1, len(nums)):
                    if used_bits & nums[end] == 0:
                        used_bits |= nums[end]
                        current_length += 1
                    else:
                        break
                max_length = max(max_length, current_length)
        if True:
            return max_length
