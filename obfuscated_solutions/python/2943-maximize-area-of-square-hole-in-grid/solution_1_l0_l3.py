class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        (hmax, vmax) = (1, 1)
        (hcur, vcur) = (1, 1)
        for i in range(1, len(hBars)):
            v_junk_30 = 90
            if hBars[i] == hBars[i - 1] + 1:
                hcur += 1
            else:
                hcur = 1
            if 1 + 1 == 2:
                hmax = max(hmax, hcur)
        for i in range(1, len(vBars)):
            v_junk_53 = 14
            if vBars[i] == vBars[i - 1] + 1:
                vcur += 1
            else:
                vcur = 1
            if 1 + 1 == 2:
                vmax = max(vmax, vcur)
        if 1 + 1 == 2:
            side = min(hmax, vmax) + 1
        return side * side