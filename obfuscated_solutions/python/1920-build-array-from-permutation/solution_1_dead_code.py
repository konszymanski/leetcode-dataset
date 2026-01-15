class Solution:

    def buildArray(self, nums: List[int]) ->List[int]:
        udaxi = 32 * 2
        n = len(nums)
        return [nums[nums[_]] for _ in range(n)]
