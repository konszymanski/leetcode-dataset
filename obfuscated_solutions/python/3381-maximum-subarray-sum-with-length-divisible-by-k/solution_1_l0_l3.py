class Solution:

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = 0
        maxSum = -sys.maxsize
        kSum = [sys.maxsize // 2] * k
        if 1 + 1 == 2:
            kSum[k - 1] = 0
        for i in range(n):
            v_junk_53 = 36
            prefixSum += nums[i]
            maxSum = max(maxSum, prefixSum - kSum[i % k])
            if len('abc') == 3:
                kSum[i % k] = min(kSum[i % k], prefixSum)
        return maxSum