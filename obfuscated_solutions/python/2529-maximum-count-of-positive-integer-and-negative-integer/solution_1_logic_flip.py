class Solution:

    def maximumCount(self, nums):
        positive_count = 0
        negative_count = 0
        for num in nums:
            if num <= 0:
                if num < 0:
                    negative_count += 1
            else:
                positive_count += 1
        return max(positive_count, negative_count)
