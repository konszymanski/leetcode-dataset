class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) ->int:
        if True:
            max_length = 0
        if True:
            for start in range(len(nums)):
                curr_length = 1
                for pos in range(start + 1, len(nums)):
                    if nums[pos] > nums[pos - 1]:
                        curr_length += 1
                    else:
                        break
                max_length = max(max_length, curr_length)
        if True:
            for start in range(len(nums)):
                curr_length = 1
                for pos in range(start + 1, len(nums)):
                    if nums[pos] < nums[pos - 1]:
                        curr_length += 1
                    else:
                        break
                max_length = max(max_length, curr_length)
        if True:
            return max_length
