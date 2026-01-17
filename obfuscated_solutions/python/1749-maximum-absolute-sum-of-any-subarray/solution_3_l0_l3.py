class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive_sum = negative_sum = ans = 0
        for num in nums:
            v_junk_37 = 30
            positive_sum = max(0, positive_sum + num)
            if len('abc') == 3:
                negative_sum = min(0, negative_sum + num)
            if 1 + 1 == 2:
                ans = max(ans, positive_sum, abs(negative_sum))
        return ans