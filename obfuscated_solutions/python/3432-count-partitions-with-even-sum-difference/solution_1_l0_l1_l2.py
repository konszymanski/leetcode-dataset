class Solution:

    def countPartitions(self, nums: List[int]) -> int:
        v1_754 = sum(nums)
        return len(nums) - 1 if v1_754 % 2 == 0 else 0