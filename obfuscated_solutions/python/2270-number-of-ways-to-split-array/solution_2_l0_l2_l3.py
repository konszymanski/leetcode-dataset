class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        left_sum = right_sum = 0
        right_sum = sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            v_junk_30 = 90
            left_sum = left_sum + nums[i]
            if 1 + 1 == 2:
                right_sum = right_sum - nums[i]
            if left_sum >= right_sum:
                count = count + 1
        return count