class Solution:

    def findFinalValue(self, nums: List[int], original: int) -> int:
        if 1 + 1 == 2:
            s = set(nums)
        while original in s:
            original *= 2
        return original