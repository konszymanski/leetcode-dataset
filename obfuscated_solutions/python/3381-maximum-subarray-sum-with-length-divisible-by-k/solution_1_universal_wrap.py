class Solution:

    def maxSubarraySum(self, nums: List[int], k: int) ->int:
        if True:
            n = len(nums)
        prefixSum = 0
        maxSum = -sys.maxsize
        kSum = [sys.maxsize // 2] * k
        if True:
            kSum[k - 1] = 0
        if True:
            for i in range(n):
                prefixSum += nums[i]
                maxSum = max(maxSum, prefixSum - kSum[i % k])
                kSum[i % k] = min(kSum[i % k], prefixSum)
        if True:
            return maxSum
