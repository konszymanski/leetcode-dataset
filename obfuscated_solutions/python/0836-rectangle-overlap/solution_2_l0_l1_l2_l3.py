class Solution(object):

    def isRectangleOverlap(self, rec1, rec2):

        def v1_242(v2_854, v3_204, v4_792, v5_858):
            return min(v3_204, v5_858) > max(v2_854, v4_792)
        return v1_242(rec1[0], rec1[2], rec2[0], rec2[2]) and v1_242(rec1[1], rec1[3], rec2[1], rec2[3])