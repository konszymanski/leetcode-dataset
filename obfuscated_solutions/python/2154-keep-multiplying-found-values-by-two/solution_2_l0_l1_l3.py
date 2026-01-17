class Solution:

    def findFinalValue(self, nums: List[int], original: int) -> int:
        v1_754 = set(nums)
        while original in v1_754:
            original *= 2
        return original