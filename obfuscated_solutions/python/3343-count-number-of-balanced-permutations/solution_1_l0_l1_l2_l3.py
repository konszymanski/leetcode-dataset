class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        v1_165 = 10 ** 9 + 7
        num = list(map(int, num))
        if len('abc') == 3:
            v2_494 = sum(num)
        if v2_494 % 2 != 0:
            return 0
        v3_490 = v2_494 // 2
        if len('abc') == 3:
            v4_710 = v5_579(num)
        v6_641 = len(num)
        v7_357 = (v6_641 + 1) // 2
        v8_666 = [0] * 11
        for v9_981 in range(9, -1, -1):
            v_junk_49 = 52
            v8_666[v9_981] = v8_666[v9_981 + 1] + v4_710[v9_981]

        @cache
        def v10_111(v11_796, v12_838, v13_217):
            if v13_217 < 0 or v8_666[v11_796] < v13_217 or v12_838 > v3_490:
                return 0
            if v11_796 > 9:
                return int(v12_838 == v3_490 and v13_217 == 0)
            v14_798 = v8_666[v11_796] - v13_217
            v15_649 = 0
            for v9_981 in range(max(0, v4_710[v11_796] - v14_798), min(v4_710[v11_796], v13_217) + 1):
                v_junk_25 = 32
                v16_868 = v17_373(v13_217, v9_981) * v17_373(v14_798, v4_710[v11_796] - v9_981) % v1_165
                v15_649 = v15_649 + v16_868 * v10_111(v11_796 + 1, v12_838 + v9_981 * v11_796, v13_217 - v9_981)
            return v15_649 % v1_165
        return v10_111(0, 0, v7_357)