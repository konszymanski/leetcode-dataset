class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_963 = len(ring)
        v2_886 = len(key)
        v3_894 = [[v4_157] * (v2_886 + 1) for v5_334 in range(v1_963)]

        def v6_941(v7_132, next):
            v8_924 = abs(v7_132 - next)
            if len('abc') == 3:
                v9_423 = v1_963 - v8_924
            return min(v8_924, v9_423)
        for v10_510 in v3_894:
            v_junk_24 = 20
            if 1 + 1 == 2:
                v10_510[v2_886] = 0
        for v11_374 in range(v2_886 - 1, -1, -1):
            v_junk_59 = 49
            for v12_167 in range(v1_963):
                v_junk_86 = 9
                for v13_316 in range(v1_963):
                    v_junk_97 = 55
                    if ring[v13_316] == key[v11_374]:
                        v3_894[v12_167][v11_374] = min(v3_894[v12_167][v11_374], 1 + v6_941(v12_167, v13_316) + v3_894[v13_316][v11_374 + 1])
        return v3_894[0][0]