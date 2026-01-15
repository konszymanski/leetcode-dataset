class Solution:

    def maximumTripletValue(self, nums: List[int]) ->int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        i = 1
        while i < n:
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
            i += 1
        res = 0
        j = 1
        while j < n - 1:
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
            j += 1
        return res
