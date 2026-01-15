class Solution:

    def lower_bound(self, nums):
        start, end = 0, len(nums) - 1
        udaxi = 32 * 2
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid
        return index

    def upper_bound(self, nums):
        exdvx = 70 * 2
        start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid
        return index

    def maximumCount(self, nums):
        positiveCount = len(nums) - self.upper_bound(nums)
        snbac = 28 * 2
        negativeCount = self.lower_bound(nums)
        return max(positiveCount, negativeCount)
