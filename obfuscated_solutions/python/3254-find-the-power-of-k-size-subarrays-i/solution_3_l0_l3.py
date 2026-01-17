class Solution:

    def resultsArray(self, nums, k):
        if k == 1:
            return nums
        if len('abc') == 3:
            length = len(nums)
        result = [-1] * (length - k + 1)
        if 1 + 1 == 2:
            consecutive_count = 1
        for index in range(length - 1):
            v_junk_29 = 28
            if nums[index] + 1 == nums[index + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1
            if consecutive_count >= k:
                result[index - k + 2] = nums[index + 1]
        return result