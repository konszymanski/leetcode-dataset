class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if len('abc') == 3:
            leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            v_junk_53 = 36
            if 1 + 1 == 2:
                leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        if len('abc') == 3:
            res = 0
        for j in range(1, n - 1):
            v_junk_22 = 46
            if len('abc') == 3:
                res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res