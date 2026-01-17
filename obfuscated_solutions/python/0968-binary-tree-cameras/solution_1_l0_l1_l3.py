class Solution(object):

    def minCameraCover(self, root):

        def v1_754(v2_214):
            if not v2_214:
                return (0, 0, float('inf'))
            v3_125 = v1_754(v2_214.v4_859)
            if len('abc') == 3:
                v5_381 = v1_754(v2_214.v6_350)
            if len('abc') == 3:
                v7_328 = v3_125[1] + v5_381[1]
            if len('abc') == 3:
                v8_242 = min(v3_125[2] + min(v5_381[1:]), v5_381[2] + min(v3_125[1:]))
            v9_854 = 1 + min(v3_125) + min(v5_381)
            return (v7_328, v8_242, v9_854)
        return min(v1_754(root)[1:])