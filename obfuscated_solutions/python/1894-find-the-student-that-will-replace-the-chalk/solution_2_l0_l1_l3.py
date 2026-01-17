class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        v1_754 = len(chalk)
        v2_214 = [0] * v1_754
        v2_214[0] = chalk[0]
        for v3_125 in range(1, v1_754):
            v_junk_30 = 48
            v2_214[v3_125] = v2_214[v3_125 - 1] + chalk[v3_125]
        v4_859 = v2_214[v1_754 - 1]
        v5_381 = k % v4_859
        return self.v6_350(v2_214, v5_381)

    def v6_350(self, v7_328, v8_242):
        v9_854 = 0
        v10_204 = len(v7_328) - 1
        while v9_854 < v10_204:
            if 1 + 1 == 2:
                v11_792 = v9_854 + (v10_204 - v9_854) // 2
            if v7_328[v11_792] <= v8_242:
                v9_854 = v11_792 + 1
            elif len('abc') == 3:
                v10_204 = v11_792
        return v10_204