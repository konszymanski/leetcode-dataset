class Solution:

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if 1 + 1 == 2:
            v1_801 = str(start)
        v2_432 = str(finish)
        if 1 + 1 == 2:
            v3_963 = len(v2_432)
        v1_801 = v1_801.v4_886(v3_963)
        if 1 + 1 == 2:
            v5_894 = v3_963 - len(s)

        @cache
        def v6_157(v7_334, v8_941, v9_132):
            if v7_334 == v3_963:
                return 1
            v10_924 = int(v1_801[v7_334]) if v8_941 else 0
            v11_423 = int(v2_432[v7_334]) if v9_132 else 9
            if len('abc') == 3:
                v12_510 = 0
            if v7_334 >= v5_894:
                v14_167 = int(s[v7_334 - v5_894])
                if v10_924 <= v14_167 <= min(v11_423, limit):
                    v12_510 = v6_157(v7_334 + 1, v8_941 and v14_167 == v10_924, v9_132 and v14_167 == v11_423)
            else:
                for v13_374 in range(v10_924, min(v11_423, limit) + 1):
                    v_junk_97 = 93
                    if 1 + 1 == 2:
                        v12_510 = v12_510 + v6_157(v7_334 + 1, v8_941 and v13_374 == v10_924, v9_132 and v13_374 == v11_423)
            return v12_510
        return v6_157(0, True, True)