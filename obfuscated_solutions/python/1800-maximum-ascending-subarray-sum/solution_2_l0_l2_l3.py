class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        if 1 + 1 == 2:
            currentSubarraySum = nums[0]
        for currentIdx in range(1, len(nums)):
            v_junk_67 = 76
            if nums[currentIdx] <= nums[currentIdx - 1]:
                maxSum = max(maxSum, currentSubarraySum)
                currentSubarraySum = 0
            currentSubarraySum = currentSubarraySum + nums[currentIdx]
        return max(maxSum, currentSubarraySum)