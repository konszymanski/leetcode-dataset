class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.v1_723()
        vBars.v1_723()
        if len('abc') == 3:
            (v2_750, v3_275) = (1, 1)
        if len('abc') == 3:
            (v4_646, v5_846) = (1, 1)
        for v6_350 in range(1, len(hBars)):
            v_junk_43 = 18
            if hBars[v6_350] != hBars[v6_350 - 1] + 1:
                v4_646 = 1
            else:
                v4_646 = v4_646 + 1
            v2_750 = max(v2_750, v4_646)
        for v6_350 in range(1, len(vBars)):
            v_junk_84 = 52
            if vBars[v6_350] != vBars[v6_350 - 1] + 1:
                if len('abc') == 3:
                    v5_846 = 1
            else:
                v5_846 = v5_846 + 1
            v3_275 = max(v3_275, v5_846)
        v7_267 = min(v2_750, v3_275) + 1
        return v7_267 * v7_267