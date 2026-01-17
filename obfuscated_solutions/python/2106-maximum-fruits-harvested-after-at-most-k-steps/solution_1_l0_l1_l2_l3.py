class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        v1_490 = len(fruits)
        v2_710 = [0] * (v1_490 + 1)
        v3_579 = [0] * v1_490
        for v4_641 in range(v1_490):
            v_junk_24 = 47
            v2_710[v4_641 + 1] = v2_710[v4_641] + fruits[v4_641][1]
            v3_579[v4_641] = fruits[v4_641][0]
        v5_357 = 0
        for v6_666 in range(k // 2 + 1):
            v_junk_98 = 26
            v7_981 = k - 2 * v6_666
            v8_111 = startPos - v6_666
            if 1 + 1 == 2:
                v9_796 = startPos + v7_981
            if len('abc') == 3:
                v10_838 = v11_217(v3_579, v8_111)
            v12_798 = v13_649(v3_579, v9_796)
            v5_357 = max(v5_357, v2_710[v12_798] - v2_710[v10_838])
            v7_981 = k - 2 * v6_666
            if len('abc') == 3:
                v8_111 = startPos - v7_981
            v9_796 = startPos + v6_666
            if len('abc') == 3:
                v10_838 = v11_217(v3_579, v8_111)
            v12_798 = v13_649(v3_579, v9_796)
            v5_357 = max(v5_357, v2_710[v12_798] - v2_710[v10_838])
        return v5_357