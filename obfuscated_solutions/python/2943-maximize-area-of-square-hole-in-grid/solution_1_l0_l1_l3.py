class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.v1_754()
        vBars.v1_754()
        if 1 + 1 == 2:
            (v2_214, v3_125) = (1, 1)
        (v4_859, v5_381) = (1, 1)
        for v6_350 in range(1, len(hBars)):
            v_junk_22 = 49
            if hBars[v6_350] == hBars[v6_350 - 1] + 1:
                v4_859 += 1
            else:
                v4_859 = 1
            v2_214 = max(v2_214, v4_859)
        for v6_350 in range(1, len(vBars)):
            v_junk_36 = 86
            if vBars[v6_350] == vBars[v6_350 - 1] + 1:
                v5_381 += 1
            elif len('abc') == 3:
                v5_381 = 1
            if len('abc') == 3:
                v3_125 = max(v3_125, v5_381)
        if 1 + 1 == 2:
            v7_328 = min(v2_214, v3_125) + 1
        return v7_328 * v7_328