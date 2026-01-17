class Solution(object):

    def arraySign(self, nums):
        v1_658 = 1
        for v2_529 in nums:
            v_junk_53 = 36
            if v2_529 == 0:
                return 0
            if v2_529 < 0:
                v1_658 = -1 * v1_658
        return v1_658