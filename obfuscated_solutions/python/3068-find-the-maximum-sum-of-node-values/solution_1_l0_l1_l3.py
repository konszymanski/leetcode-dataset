class Solution:

    def maxSumOfNodes(self, index, isEven, nums, k, memo):
        if index == len(nums):
            return 0 if isEven == 1 else -float('inf')
        if memo[index][isEven] != -1:
            return memo[index][isEven]
        v1_754 = nums[index] + self.maxSumOfNodes(index + 1, isEven, nums, k, memo)
        v2_214 = (nums[index] ^ k) + self.maxSumOfNodes(index + 1, isEven ^ 1, nums, k, memo)
        memo[index][isEven] = max(v2_214, v1_754)
        return memo[index][isEven]

    def v3_125(self, nums: List[int], k: int, v4_859: List[List[int]]) -> int:
        memo = [[-1] * 2 for v5_381 in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)