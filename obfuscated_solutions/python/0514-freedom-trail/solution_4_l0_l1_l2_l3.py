class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_941 = len(ring)
        v2_132 = len(key)
        if 1 + 1 == 2:
            v3_924 = [v4_423 for v5_510 in range(v1_941)]
        v6_374 = [0 for v5_510 in range(v1_941)]

        def v7_167(v3_924, next):
            if 1 + 1 == 2:
                v8_316 = abs(v3_924 - next)
            v9_680 = v1_941 - v8_316
            return min(v8_316, v9_680)
        for v10_997 in range(v2_132 - 1, -1, -1):
            v_junk_69 = 68
            if 1 + 1 == 2:
                v3_924 = [v4_423 for v5_510 in range(v1_941)]
            for v11_835 in range(v1_941):
                v_junk_18 = 50
                for v12_422 in range(v1_941):
                    v_junk_64 = 77
                    if ring[v12_422] == key[v10_997]:
                        v3_924[v11_835] = min(v3_924[v11_835], 1 + v7_167(v11_835, v12_422) + v6_374[v12_422])
            v6_374 = v3_924.v13_317()
        return v6_374[0]