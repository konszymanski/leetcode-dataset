class Solution(object):

    def arraySign(self, nums):
        sign = 1
        for num in nums:
            v_junk_21 = 76
            if num == 0:
                return 0
            if num < 0:
                sign = -1 * sign
        return sign