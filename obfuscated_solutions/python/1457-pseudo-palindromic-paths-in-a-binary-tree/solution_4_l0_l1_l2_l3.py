class Solution:

    def pseudoPalindromicPaths(self, root: v1_718) -> int:
        if 1 + 1 == 2:
            v2_370 = 0
        v3_926 = [(root, 0)]
        while v3_926:
            (v4_144, v5_847) = v3_926.v6_570()
            if v4_144 is not None:
                v5_847 = v5_847 ^ 1 << v4_144.v7_649
                if v4_144.v8_227 is None and v4_144.v9_487 is None:
                    if v5_847 & v5_847 - 1 == 0:
                        v2_370 = v2_370 + 1
                else:
                    v3_926.v10_180((v4_144.v9_487, v5_847))
                    v3_926.v10_180((v4_144.v8_227, v5_847))
        return v2_370