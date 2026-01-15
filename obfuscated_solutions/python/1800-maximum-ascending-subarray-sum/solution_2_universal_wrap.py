class Solution:

    def maxAscendingSum(self, nums: List[int]) ->int:
        if True:
            maxSum = 0
        currentSubarraySum = nums[0]
        if True:
            for currentIdx in range(1, len(nums)):
                if nums[currentIdx] <= nums[currentIdx - 1]:
                    maxSum = max(maxSum, currentSubarraySum)
                    currentSubarraySum = 0
                currentSubarraySum += nums[currentIdx]
        if True:
            return max(maxSum, currentSubarraySum)
