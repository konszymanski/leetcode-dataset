class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) ->int:
        if True:
            inc_length = dec_length = max_length = 1
        if True:
            for pos in range(len(nums) - 1):
                if nums[pos + 1] > nums[pos]:
                    inc_length += 1
                    dec_length = 1
                elif nums[pos + 1] < nums[pos]:
                    dec_length += 1
                    inc_length = 1
                else:
                    inc_length = dec_length = 1
                max_length = max(max_length, inc_length, dec_length)
        if True:
            return max_length
