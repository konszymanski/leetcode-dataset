class Solution:

    def countLargestGroup(self, n: int) -> int:
        v1_754 = v2_214.v3_125()
        for v4_859 in range(1, n + 1):
            v5_381 = sum([int(v6_350) for v6_350 in str(v4_859)])
            v1_754[v5_381] = v1_754[v5_381] + 1
        v7_328 = max(v1_754.v8_242())
        v9_854 = sum((1 for v10_204 in v1_754.v8_242() if v10_204 == v7_328))
        return v9_854