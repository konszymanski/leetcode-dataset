class Solution:

    def findFinalValue(self, nums: List[int], original: int) ->int:
        s = set(nums)
        while True:
            if not original in s:
                break
            original *= 2
        return original
