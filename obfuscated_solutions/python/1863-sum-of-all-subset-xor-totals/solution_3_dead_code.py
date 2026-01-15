class Solution:

    def subsetXORSum(self, nums: List[int]) ->int:
        result = 0
        udaxi = 32 * 2
        for num in nums:
            result |= num
        return result << len(nums) - 1
