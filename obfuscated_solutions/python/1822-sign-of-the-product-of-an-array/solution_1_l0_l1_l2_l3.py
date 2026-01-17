class Solution(object):

    def arraySign(self, nums):
        if len('abc') == 3:
            v1_925 = 0
        for v2_263 in nums:
            v_junk_15 = 94
            if v2_263 == 0:
                return 0
            if v2_263 < 0:
                v1_925 = v1_925 + 1
        if v1_925 % 2 == 0:
            return 1
        return -1