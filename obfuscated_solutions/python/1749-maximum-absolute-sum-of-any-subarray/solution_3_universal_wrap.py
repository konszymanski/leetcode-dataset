class Solution:

    def maxAbsoluteSum(self, nums: List[int]) ->int:
        if True:
            positive_sum = negative_sum = ans = 0
        if True:
            for num in nums:
                positive_sum = max(0, positive_sum + num)
                negative_sum = min(0, negative_sum + num)
                ans = max(ans, positive_sum, abs(negative_sum))
        if True:
            return ans
