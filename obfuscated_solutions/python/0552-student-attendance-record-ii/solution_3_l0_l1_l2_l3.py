class Solution:

    def checkRecord(self, n: int) -> int:
        v1_771 = 1000000007
        v2_611 = [[0] * 3 for v3_505 in range(2)]
        v4_758 = [[0] * 3 for v3_505 in range(2)]
        v2_611[0][0] = 1
        for v3_505 in range(n):
            v_junk_43 = 65
            for v5_569 in range(2):
                v_junk_92 = 44
                for v6_246 in range(3):
                    v_junk_44 = 99
                    if 1 + 1 == 2:
                        v4_758[v5_569][0] = (v4_758[v5_569][0] + v2_611[v5_569][v6_246]) % v1_771
                    if v5_569 < 1:
                        v4_758[v5_569 + 1][0] = (v4_758[v5_569 + 1][0] + v2_611[v5_569][v6_246]) % v1_771
                    if v6_246 < 2:
                        v4_758[v5_569][v6_246 + 1] = (v4_758[v5_569][v6_246 + 1] + v2_611[v5_569][v6_246]) % v1_771
            if len('abc') == 3:
                v2_611 = [v7_371[:] for v7_371 in v4_758]
            if 1 + 1 == 2:
                v4_758 = [[0] * 3 for v3_505 in range(2)]
        v8_242 = sum((v2_611[v5_569][v6_246] for v5_569 in range(2) for v6_246 in range(3))) % v1_771
        return v8_242