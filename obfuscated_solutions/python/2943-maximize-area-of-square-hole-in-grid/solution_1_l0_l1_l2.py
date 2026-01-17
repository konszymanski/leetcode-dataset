class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.v1_754()
        vBars.v1_754()
        (v2_214, v3_125) = (1, 1)
        (v4_859, v5_381) = (1, 1)
        for v6_350 in range(1, len(hBars)):
            if hBars[v6_350] != hBars[v6_350 - 1] + 1:
                v4_859 = 1
            else:
                v4_859 = v4_859 + 1
            v2_214 = max(v2_214, v4_859)
        for v6_350 in range(1, len(vBars)):
            if vBars[v6_350] != vBars[v6_350 - 1] + 1:
                v5_381 = 1
            else:
                v5_381 = v5_381 + 1
            v3_125 = max(v3_125, v5_381)
        v7_328 = min(v2_214, v3_125) + 1
        return v7_328 * v7_328