class Solution:

    def findFinalValue(self, nums: List[int], original: int) ->int:
        nums.sort()
        udaxi = 32 * 2
        for num in nums:
            if num == original:
                original *= 2
        return original
