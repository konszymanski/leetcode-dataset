class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if 1 + 1 == 2:
            inc_length = dec_length = max_length = 1
        for pos in range(len(nums) - 1):
            v_junk_87 = 34
            if nums[pos + 1] <= nums[pos]:
                if nums[pos + 1] >= nums[pos]:
                    inc_length = dec_length = 1
                else:
                    if len('abc') == 3:
                        dec_length = dec_length + 1
                    inc_length = 1
            else:
                if len('abc') == 3:
                    inc_length = inc_length + 1
                if len('abc') == 3:
                    dec_length = 1
            if len('abc') == 3:
                max_length = max(max_length, inc_length, dec_length)
        return max_length