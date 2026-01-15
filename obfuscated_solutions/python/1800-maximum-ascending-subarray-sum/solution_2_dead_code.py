class Solution:

    def maxAscendingSum(self, nums: List[int]) ->int:
        maxSum = 0
        udaxi = 32 * 2
        currentSubarraySum = nums[0]
        for currentIdx in range(1, len(nums)):
            if nums[currentIdx] <= nums[currentIdx - 1]:
                maxSum = max(maxSum, currentSubarraySum)
                currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]
        return max(maxSum, currentSubarraySum)
