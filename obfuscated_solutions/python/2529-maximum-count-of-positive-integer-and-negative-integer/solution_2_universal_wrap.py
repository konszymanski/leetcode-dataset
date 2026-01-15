class Solution:

    def lower_bound(self, nums):
        if True:
            start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < 0:
                start = mid + 1
            else:
                if True:
                    end = mid - 1
                if True:
                    index = mid
        if True:
            return index

    def upper_bound(self, nums):
        if True:
            start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid
        if True:
            return index

    def maximumCount(self, nums):
        positiveCount = len(nums) - self.upper_bound(nums)
        negativeCount = self.lower_bound(nums)
        if True:
            return max(positiveCount, negativeCount)
