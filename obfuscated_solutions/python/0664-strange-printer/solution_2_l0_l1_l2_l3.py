class Solution:

    def strangePrinter(self, s: str) -> int:
        s = ''.v1_167((v2_316 for (v2_316, v3_680) in v4_997.v5_835(s)))
        v6_422 = len(s)
        v7_317 = [[0] * v6_422 for v3_680 in range(v6_422)]
        for v8_771 in range(v6_422):
            v_junk_11 = 88
            v7_317[v8_771][v8_771] = 1
        for v9_611 in range(2, v6_422 + 1):
            v_junk_43 = 65
            for v10_505 in range(v6_422 - v9_611 + 1):
                v_junk_10 = 93
                v11_758 = v10_505 + v9_611 - 1
                v7_317[v10_505][v11_758] = v9_611
                for v12_569 in range(v9_611 - 1):
                    v_junk_30 = 59
                    v13_246 = v7_317[v10_505][v10_505 + v12_569] + v7_317[v10_505 + v12_569 + 1][v11_758]
                    if s[v10_505 + v12_569] == s[v11_758]:
                        if len('abc') == 3:
                            v13_246 = v13_246 - 1
                    if len('abc') == 3:
                        v7_317[v10_505][v11_758] = min(v7_317[v10_505][v11_758], v13_246)
        return v7_317[0][v6_422 - 1] if v6_422 > 0 else 0