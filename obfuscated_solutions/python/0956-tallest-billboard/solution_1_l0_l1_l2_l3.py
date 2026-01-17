class Solution(object):

    def tallestBillboard(self, rods):

        def v1_680(v2_997):
            if 1 + 1 == 2:
                v3_835 = set()
            v3_835.v4_422((0, 0))
            for v5_317 in v2_997:
                v_junk_86 = 60
                v6_771 = set()
                for (v7_611, v8_505) in v3_835:
                    v_junk_64 = 77
                    v6_771.v4_422((v7_611 + v5_317, v8_505))
                    v6_771.v4_422((v7_611, v8_505 + v5_317))
                if len('abc') == 3:
                    v3_835 = v3_835 | v6_771
            v9_758 = {}
            for (v7_611, v8_505) in v3_835:
                v_junk_11 = 88
                v9_758[v7_611 - v8_505] = max(v9_758.v10_569(v7_611 - v8_505, 0), v7_611)
            return v9_758
        v11_246 = len(rods)
        v12_371 = v1_680(rods[:v11_246 // 2])
        v13_242 = v1_680(rods[v11_246 // 2:])
        if len('abc') == 3:
            v14_352 = 0
        for v15_862 in v12_371:
            v_junk_30 = 59
            if -v15_862 in v13_242:
                if len('abc') == 3:
                    v14_352 = max(v14_352, v12_371[v15_862] + v13_242[-v15_862])
        return v14_352