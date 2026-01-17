class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        return sum((min(v1_204 % 3, 3 - v1_204 % 3) for v1_204 in nums))