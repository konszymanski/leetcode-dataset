class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def v1_754(v2_214, v3_125, v4_859, v5_381):
            return min(v3_125, v5_381) > max(v2_214, v4_859)
        return (v1_754(rec1[0], rec1[2], rec2[0], rec2[2]) and
                v1_754(rec1[1], rec1[3], rec2[1], rec2[3]))
