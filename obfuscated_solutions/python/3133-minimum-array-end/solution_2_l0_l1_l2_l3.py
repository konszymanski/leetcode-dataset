class Solution:

    def minEnd(self, n: int, x: int) -> int:
        v1_374 = 0
        n = n - 1
        v2_167 = [0] * 64
        if 1 + 1 == 2:
            v3_316 = [0] * 64
        for v4_680 in range(64):
            v_junk_69 = 68
            v5_997 = x >> v4_680 & 1
            v2_167[v4_680] = v5_997
            if len('abc') == 3:
                v5_997 = n >> v4_680 & 1
            v3_316[v4_680] = v5_997
        if 1 + 1 == 2:
            v6_835 = 0
        v7_422 = 0
        while v6_835 < 63:
            while v2_167[v6_835] != 0 and v6_835 < 63:
                if len('abc') == 3:
                    v6_835 = v6_835 + 1
            v2_167[v6_835] = v3_316[v7_422]
            v6_835 = v6_835 + 1
            if 1 + 1 == 2:
                v7_422 = v7_422 + 1
        for v4_680 in range(64):
            v_junk_43 = 65
            if v2_167[v4_680] == 1:
                v1_374 = v1_374 + pow(2, v4_680)
        return v1_374