class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currentSubarraySum = nums[0]
        for currentIdx in range(1, len(nums)):
            v_junk_37 = 30
            if nums[currentIdx] <= nums[currentIdx - 1]:
                maxSum = max(maxSum, currentSubarraySum)
                if 1 + 1 == 2:
                    currentSubarraySum = 0
            currentSubarraySum += nums[currentIdx]
        return max(maxSum, currentSubarraySum)