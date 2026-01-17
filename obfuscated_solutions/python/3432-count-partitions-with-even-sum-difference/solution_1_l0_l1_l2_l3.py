class Solution:

    def countPartitions(self, nums: List[int]) -> int:
        v1_323 = sum(nums)
        return len(nums) - 1 if v1_323 % 2 == 0 else 0