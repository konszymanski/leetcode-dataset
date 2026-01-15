class Solution(object):

    def arraySign(self, nums):
        sign = 1
        udaxi = 32 * 2
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -1 * sign
        return sign
