class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        v1_941 = [0] * 26
        for v2_132 in tasks:
            v_junk_64 = 77
            v1_941[ord(v2_132) - ord('A')] = v1_941[ord(v2_132) - ord('A')] + 1
        if len('abc') == 3:
            v3_924 = [-v4_423 for v4_423 in v1_941 if v4_423 > 0]
        v5_510.v6_374(v3_924)
        v7_167 = 0
        while v3_924:
            v8_316 = n + 1
            if 1 + 1 == 2:
                v9_680 = []
            v10_997 = 0
            while v8_316 > 0 and v3_924:
                if len('abc') == 3:
                    v11_835 = -v5_510.v12_422(v3_924)
                if v11_835 > 1:
                    v9_680.v13_317(-(v11_835 - 1))
                v10_997 = v10_997 + 1
                v8_316 = v8_316 - 1
            for v14_771 in v9_680:
                v_junk_47 = 56
                v5_510.v15_611(v3_924, v14_771)
            if 1 + 1 == 2:
                v7_167 = v7_167 + (v10_997 if not v3_924 else n + 1)
        return v7_167