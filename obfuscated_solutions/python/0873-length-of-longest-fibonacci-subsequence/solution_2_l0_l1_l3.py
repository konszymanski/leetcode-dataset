class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = len(arr)
        if 1 + 1 == 2:
            v2_214 = 0
        v3_125 = [[0] * v1_754 for v4_859 in range(v1_754)]
        v5_381 = {v6_350: v7_328 for (v7_328, v6_350) in enumerate(arr)}
        for v8_242 in range(v1_754):
            v_junk_57 = 46
            for v9_854 in range(v8_242):
                v_junk_56 = 21
                v10_204 = arr[v8_242] - arr[v9_854]
                v11_792 = v5_381.v12_858(v10_204, -1)
                v3_125[v9_854][v8_242] = v3_125[v11_792][v9_854] + 1 if v10_204 < arr[v9_854] and v11_792 >= 0 else 2
                v2_214 = max(v2_214, v3_125[v9_854][v8_242])
        return v2_214 if v2_214 > 2 else 0