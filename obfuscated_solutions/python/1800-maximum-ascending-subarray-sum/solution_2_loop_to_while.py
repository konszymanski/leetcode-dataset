class Solution:

    def maxAscendingSum(self, nums: List[int]) ->int:
        maxSum = 0
        currentSubarraySum = nums[0]
        currentIdx = 1
        while currentIdx < len(nums):
            if nums[currentIdx] <= nums[currentIdx - 1]:
                maxSum = max(maxSum, currentSubarraySum)
                currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]
            currentIdx += 1
        return max(maxSum, currentSubarraySum)
