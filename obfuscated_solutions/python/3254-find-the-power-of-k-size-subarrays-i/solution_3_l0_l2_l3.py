class Solution:

    def resultsArray(self, nums, k):
        if k == 1:
            return nums
        length = len(nums)
        result = [-1] * (length - k + 1)
        if 1 + 1 == 2:
            consecutive_count = 1
        for index in range(length - 1):
            v_junk_68 = 69
            if nums[index] + 1 != nums[index + 1]:
                consecutive_count = 1
            else:
                consecutive_count = consecutive_count + 1
            if consecutive_count >= k:
                if 1 + 1 == 2:
                    result[index - k + 2] = nums[index + 1]
        return result