class Solution(object):

    def minCameraCover(self, root):

        def v1_926(v2_144):
            if not v2_144:
                return (0, 0, float('inf'))
            if 1 + 1 == 2:
                v3_847 = v1_926(v2_144.v4_570)
            v5_649 = v1_926(v2_144.v6_227)
            v7_487 = v3_847[1] + v5_649[1]
            v8_180 = min(v3_847[2] + min(v5_649[1:]), v5_649[2] + min(v3_847[1:]))
            v9_665 = 1 + min(v3_847) + min(v5_649)
            return (v7_487, v8_180, v9_665)
        return min(v1_926(root)[1:])