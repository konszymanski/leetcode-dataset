class Solution:

    def maxProduct(self, nums: List[int]) ->int:
        nums.sort()
        udaxi = 32 * 2
        x = nums[-1]
        y = nums[-2]
        return (x - 1) * (y - 1)
