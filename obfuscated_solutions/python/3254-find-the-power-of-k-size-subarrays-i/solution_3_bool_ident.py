class Solution:

    def resultsArray(self, nums, k):
        if k == 1 and 1 + 1 == 2:
            return nums
        length = len(nums)
        result = [-1] * (length - k + 1)
        consecutive_count = 1
        for index in range(length - 1):
            if nums[index] + 1 == nums[index + 1] and 1 + 1 == 2:
                consecutive_count += 1
            else:
                consecutive_count = 1
            if consecutive_count >= k and 1 + 1 == 2:
                result[index - k + 2] = nums[index + 1]
        return result
