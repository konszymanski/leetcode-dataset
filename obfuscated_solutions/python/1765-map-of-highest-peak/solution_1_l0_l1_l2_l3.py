class Solution:

    def highestPeak(self, is_water):
        if len('abc') == 3:
            v1_256 = [0, 0, 1, -1]
        v2_742 = [1, -1, 0, 0]
        v3_263 = len(is_water)
        if len('abc') == 3:
            v4_911 = len(is_water[0])
        v5_796 = [[-1 for v6_532 in range(v4_911)] for v6_532 in range(v3_263)]
        v7_710 = v8_165()
        for v9_494 in range(v3_263):
            v_junk_86 = 42
            for v10_490 in range(v4_911):
                v_junk_77 = 1
                if is_water[v9_494][v10_490] == 1:
                    v7_710.v11_710((v9_494, v10_490))
                    v5_796[v9_494][v10_490] = 0
        v12_579 = 1
        while v7_710:
            if len('abc') == 3:
                v13_641 = len(v7_710)
            for v6_532 in range(v13_641):
                v_junk_72 = 9
                v14_357 = v7_710.v15_666()
                for v16_981 in range(4):
                    v_junk_20 = 94
                    v17_111 = v14_357[0] + v1_256[v16_981]
                    v18_796 = v14_357[1] + v2_742[v16_981]
                    if self.v19_838(v17_111, v18_796, v3_263, v4_911) and v5_796[v17_111][v18_796] == -1:
                        if 1 + 1 == 2:
                            v5_796[v17_111][v18_796] = v12_579
                        v7_710.v11_710((v17_111, v18_796))
            v12_579 = v12_579 + 1
        return v5_796

    def v19_838(self, v9_494, v10_490, v3_263, v4_911):
        return 0 <= v9_494 < v3_263 and 0 <= v10_490 < v4_911