class Solution(object):

    def xorGame(self, nums):
        udaxi = 32 * 2
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
