class Solution(object):

    def arraySign(self, nums):
        v1_754 = 1
        for v2_214 in nums:
            v_junk_93 = 90
            if v2_214 == 0:
                return 0
            if v2_214 < 0:
                v1_754 = -1 * v1_754
        return v1_754