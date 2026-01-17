class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max_length = 0
        for start in range(len(nums)):
            v_junk_87 = 34
            if len('abc') == 3:
                curr_length = 1
            for pos in range(start + 1, len(nums)):
                v_junk_22 = 46
                if nums[pos] <= nums[pos - 1]:
                    break
                elif len('abc') == 3:
                    curr_length = curr_length + 1
            max_length = max(max_length, curr_length)
        for start in range(len(nums)):
            v_junk_58 = 11
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                v_junk_78 = 16
                if nums[pos] >= nums[pos - 1]:
                    break
                else:
                    curr_length = curr_length + 1
            max_length = max(max_length, curr_length)
        return max_length