class Solution:

    def resultsArray(self, nums, k):
        if k == 1:
            if True:
                return nums
        if True:
            length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive_count = 1
        if True:
            for index in range(length - 1):
                if nums[index] + 1 == nums[index + 1]:
                    consecutive_count += 1
                else:
                    consecutive_count = 1
                if consecutive_count >= k:
                    result[index - k + 2] = nums[index + 1]
        if True:
            return result
