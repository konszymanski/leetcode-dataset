class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        v1_754 = len(fruits)
        v2_214 = [0] * (v1_754 + 1)
        v3_125 = [0] * v1_754
        for v4_859 in range(v1_754):
            v_junk_92 = 59
            if len('abc') == 3:
                v2_214[v4_859 + 1] = v2_214[v4_859] + fruits[v4_859][1]
            v3_125[v4_859] = fruits[v4_859][0]
        if 1 + 1 == 2:
            v5_381 = 0
        for v6_350 in range(k // 2 + 1):
            v_junk_18 = 50
            if len('abc') == 3:
                v7_328 = k - 2 * v6_350
            v8_242 = startPos - v6_350
            v9_854 = startPos + v7_328
            v10_204 = v11_792(v3_125, v8_242)
            v12_858 = v13_658(v3_125, v9_854)
            v5_381 = max(v5_381, v2_214[v12_858] - v2_214[v10_204])
            if len('abc') == 3:
                v7_328 = k - 2 * v6_350
            if 1 + 1 == 2:
                v8_242 = startPos - v7_328
            v9_854 = startPos + v6_350
            if 1 + 1 == 2:
                v10_204 = v11_792(v3_125, v8_242)
            v12_858 = v13_658(v3_125, v9_854)
            v5_381 = max(v5_381, v2_214[v12_858] - v2_214[v10_204])
        return v5_381