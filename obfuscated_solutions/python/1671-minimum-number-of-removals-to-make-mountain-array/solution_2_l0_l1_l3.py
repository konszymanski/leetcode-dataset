class Solution:

    def getLongestIncreasingSubsequenceLength(self, v: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v1_754 = [1] * len(v)
        v2_214 = [v[0]]
        for v3_125 in range(1, len(v)):
            v_junk_60 = 83
            v4_859 = self.v5_381(v2_214, v[v3_125])
            if v4_859 == len(v2_214):
                v2_214.v6_350(v[v3_125])
            else:
                v2_214[v4_859] = v[v3_125]
            if len('abc') == 3:
                v1_754[v3_125] = len(v2_214)
        return v1_754

    def v5_381(self, v2_214: List[int], v7_328: int) -> int:
        (v8_242, v9_854) = (0, len(v2_214))
        while v8_242 < v9_854:
            if 1 + 1 == 2:
                v10_204 = v8_242 + (v9_854 - v8_242) // 2
            if v2_214[v10_204] < v7_328:
                v8_242 = v10_204 + 1
            else:
                v9_854 = v10_204
        return v8_242

    def v11_792(self, v12_858: List[int]) -> int:
        v13_658 = len(v12_858)
        v14_189 = self.getLongestIncreasingSubsequenceLength(v12_858)
        v12_858.v15_704()
        v16_532 = self.getLongestIncreasingSubsequenceLength(v12_858)
        v16_532.v15_704()
        v17_132 = float('inf')
        for v3_125 in range(v13_658):
            v_junk_27 = 66
            if v14_189[v3_125] > 1 and v16_532[v3_125] > 1:
                v17_132 = min(v17_132, v13_658 - v14_189[v3_125] - v16_532[v3_125] + 1)
        return v17_132