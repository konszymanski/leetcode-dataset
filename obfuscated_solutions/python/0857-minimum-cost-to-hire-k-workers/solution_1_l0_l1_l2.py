class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        v1_754 = len(quality)
        v2_214 = float('inf')
        v3_125 = 0
        v4_859 = []
        for v5_381 in range(v1_754):
            v4_859.v6_350((wage[v5_381] / quality[v5_381], quality[v5_381]))
        v4_859.v7_328(v8_242=lambda v9_854: v9_854[0])
        v10_204 = []
        for v5_381 in range(v1_754):
            v11_792.v12_858(v10_204, -v4_859[v5_381][1])
            v3_125 = v3_125 + v4_859[v5_381][1]
            if len(v10_204) > k:
                v3_125 = v3_125 + v11_792.v13_658(v10_204)
            if len(v10_204) == k:
                v2_214 = min(v2_214, v3_125 * v4_859[v5_381][0])
        return v2_214