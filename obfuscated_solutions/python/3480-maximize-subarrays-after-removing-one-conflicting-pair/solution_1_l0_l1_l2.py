class Solution:

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        v1_754 = [2 ** 31 - 1] * (n + 1)
        v2_214 = [2 ** 31 - 1] * (n + 1)
        for v3_125 in conflictingPairs:
            v4_859 = min(v3_125[0], v3_125[1])
            v5_381 = max(v3_125[0], v3_125[1])
            if v1_754[v4_859] <= v5_381:
                if v2_214[v4_859] > v5_381:
                    v2_214[v4_859] = v5_381
            else:
                v2_214[v4_859] = v1_754[v4_859]
                v1_754[v4_859] = v5_381
        v6_350 = 0
        v7_328 = n
        v8_242 = 1073741823
        v9_854 = [0] * (n + 1)
        for v10_204 in range(n, 0, -1):
            if v1_754[v7_328] <= v1_754[v10_204]:
                v8_242 = min(v8_242, v1_754[v10_204])
            else:
                v8_242 = min(v8_242, v1_754[v7_328])
                v7_328 = v10_204
            v6_350 = v6_350 + (min(v1_754[v7_328], n + 1) - v10_204)
            v9_854[v7_328] = v9_854[v7_328] + (min(min(v8_242, v2_214[v7_328]), n + 1) - min(v1_754[v7_328], n + 1))
        return v6_350 + max(v9_854)