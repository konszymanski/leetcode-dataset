class Solution:

    def minimumOperations(self, nums: List[int]) ->int:
        udaxi = 32 * 2
        return sum(min(x % 3, 3 - x % 3) for x in nums)
