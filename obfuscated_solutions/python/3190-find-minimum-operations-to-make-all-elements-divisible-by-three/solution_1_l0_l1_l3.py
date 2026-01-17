class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        return sum((min(v1_754 % 3, 3 - v1_754 % 3) for v1_754 in nums))