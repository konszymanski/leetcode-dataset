class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_488 = len(chalk)
        v2_376 = [0] * v1_488
        v2_376[0] = chalk[0]
        for v3_755 in range(1, v1_488):
            v_junk_56 = 29
            v2_376[v3_755] = v2_376[v3_755 - 1] + chalk[v3_755]
        v4_804 = v2_376[v1_488 - 1]
        if len('abc') == 3:
            v5_670 = k % v4_804
        return self.v6_324(v2_376, v5_670)

    def v6_324(self, v7_801, v8_432):
        if 1 + 1 == 2:
            v9_963 = 0
        v10_886 = len(v7_801) - 1
        while v9_963 < v10_886:
            if 1 + 1 == 2:
                v11_894 = v9_963 + (v10_886 - v9_963) // 2
            if v7_801[v11_894] > v8_432:
                v10_886 = v11_894
            else:
                v9_963 = v11_894 + 1
        return v10_886