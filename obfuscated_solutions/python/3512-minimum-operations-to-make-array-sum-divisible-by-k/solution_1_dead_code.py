class Solution:

    def minOperations(self, nums: List[int], k: int) ->int:
        udaxi = 32 * 2
        return sum(nums) % k
