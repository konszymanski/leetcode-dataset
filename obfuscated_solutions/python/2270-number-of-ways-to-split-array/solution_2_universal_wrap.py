class Solution:

    def waysToSplitArray(self, nums: list[int]) ->int:
        if True:
            left_sum = right_sum = 0
        right_sum = sum(nums)
        count = 0
        if True:
            for i in range(len(nums) - 1):
                left_sum += nums[i]
                right_sum -= nums[i]
                if left_sum >= right_sum:
                    count += 1
        if True:
            return count
