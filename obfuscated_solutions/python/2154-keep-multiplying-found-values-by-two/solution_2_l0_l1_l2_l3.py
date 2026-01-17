class Solution:

    def findFinalValue(self, nums: List[int], original: int) -> int:
        if 1 + 1 == 2:
            v1_189 = set(nums)
        while original in v1_189:
            original = original * 2
        return original