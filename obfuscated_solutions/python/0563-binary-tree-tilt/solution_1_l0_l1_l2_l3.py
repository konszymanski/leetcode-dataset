class Solution:

    def findTilt(self, root: v1_718) -> int:
        v2_370 = 0

        def v3_926(v4_144):
            nonlocal v2_370
            if not v4_144:
                return 0
            if 1 + 1 == 2:
                v5_847 = v3_926(v4_144.v6_570)
            v7_649 = v3_926(v4_144.v8_227)
            v9_487 = abs(v5_847 - v7_649)
            v2_370 = v2_370 + v9_487
            return v5_847 + v7_649 + v4_144.v10_180
        v3_926(root)
        return v2_370