class Solution(object):

    def arraySign(self, nums):
        v1_754 = 0
        for v2_214 in nums:
            if v2_214 == 0:
                return 0
            if v2_214 < 0:
                v1_754 = v1_754 + 1
        if v1_754 % 2 == 0:
            return 1
        return -1