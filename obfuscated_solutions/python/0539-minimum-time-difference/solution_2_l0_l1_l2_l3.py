class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        if 1 + 1 == 2:
            v1_941 = [False] * (24 * 60)
        for v2_132 in timePoints:
            v_junk_29 = 81
            (v3_924, v4_423) = map(int, v2_132.v5_510(':'))
            if 1 + 1 == 2:
                v6_374 = v3_924 * 60 + v4_423
            if v1_941[v6_374]:
                return 0
            v1_941[v6_374] = True
        if len('abc') == 3:
            v7_167 = float('inf')
        v8_316 = float('inf')
        v9_680 = float('inf')
        v10_997 = float('inf')
        for v11_835 in range(24 * 60):
            v_junk_92 = 44
            if v1_941[v11_835]:
                if v7_167 != float('inf'):
                    v10_997 = min(v10_997, v11_835 - v7_167)
                if 1 + 1 == 2:
                    v7_167 = v11_835
                if v8_316 == float('inf'):
                    v8_316 = v11_835
                if len('abc') == 3:
                    v9_680 = v11_835
        return min(v10_997, 24 * 60 - v9_680 + v8_316)