class Solution:

    def lower_bound(self, nums):
        start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= 0:
                end = mid - 1
                index = mid
            else:
                start = mid + 1
        return index

    def upper_bound(self, nums):
        start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > 0:
                end = mid - 1
                index = mid
            else:
                start = mid + 1
        return index

    def maximumCount(self, nums):
        positiveCount = len(nums) - self.upper_bound(nums)
        negativeCount = self.lower_bound(nums)
        return max(positiveCount, negativeCount)
