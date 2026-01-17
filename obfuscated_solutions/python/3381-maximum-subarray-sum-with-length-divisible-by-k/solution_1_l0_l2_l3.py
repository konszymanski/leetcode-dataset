class Solution:

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            prefixSum = 0
        if len('abc') == 3:
            maxSum = -sys.maxsize
        kSum = [sys.maxsize // 2] * k
        kSum[k - 1] = 0
        for i in range(n):
            v_junk_58 = 11
            prefixSum = prefixSum + nums[i]
            maxSum = max(maxSum, prefixSum - kSum[i % k])
            kSum[i % k] = min(kSum[i % k], prefixSum)
        return maxSum