class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        if True:
            for i in range(1, n):
                leftMax[i] = max(leftMax[i - 1], nums[i - 1])
                rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        if True:
            for j in range(1, n - 1):
                res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        if True:
            return res
