class Solution:

    def countPartitions(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            totalSum = sum(nums)
        return len(nums) - 1 if totalSum % 2 == 0 else 0