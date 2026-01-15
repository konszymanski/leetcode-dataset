class Solution:

    def maxAscendingSum(self, nums: List[int]) ->int:
        maxSum = 0
        currentSubarraySum = nums[0]
        for currentIdx in range(1, len(nums)):
            if nums[currentIdx] <= nums[currentIdx - 1] and 1 + 1 == 2:
                maxSum = max(maxSum, currentSubarraySum)
                currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]
        return max(maxSum, currentSubarraySum)
