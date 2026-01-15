class Solution:

    def minimumOperations(self, nums: List[int]) ->int:
        if True:
            return sum(min(x % 3, 3 - x % 3) for x in nums)
