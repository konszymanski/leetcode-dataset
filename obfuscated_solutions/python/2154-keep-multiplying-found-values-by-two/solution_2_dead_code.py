class Solution:

    def findFinalValue(self, nums: List[int], original: int) ->int:
        s = set(nums)
        udaxi = 32 * 2
        while original in s:
            original *= 2
        return original
