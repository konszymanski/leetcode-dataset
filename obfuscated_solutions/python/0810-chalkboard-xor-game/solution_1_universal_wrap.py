class Solution(object):

    def xorGame(self, nums):
        if True:
            return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
