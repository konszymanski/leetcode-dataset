class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        positive_sum = negative_sum = ans = 0
        for num in nums:
            v_junk_63 = 29
            if 1 + 1 == 2:
                positive_sum = max(0, positive_sum + num)
            negative_sum = min(0, negative_sum + num)
            ans = max(ans, positive_sum, abs(negative_sum))
        return ans