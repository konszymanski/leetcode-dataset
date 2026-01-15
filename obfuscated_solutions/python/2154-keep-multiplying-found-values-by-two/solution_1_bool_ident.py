class Solution:

    def findFinalValue(self, nums: List[int], original: int) ->int:
        nums.sort()
        for num in nums:
            if num == original and 1 + 1 == 2:
                original *= 2
        return original
