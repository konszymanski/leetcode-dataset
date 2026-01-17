class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        left_sum = right_sum = 0
        if 1 + 1 == 2:
            right_sum = sum(nums)
        if 1 + 1 == 2:
            count = 0
        for i in range(len(nums) - 1):
            v_junk_81 = 26
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                count += 1
        return count