class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int],
        vBars: List[int]) ->int:
        hBars.sort()
        vBars.sort()
        if True:
            hmax, vmax = 1, 1
        hcur, vcur = 1, 1
        if True:
            for i in range(1, len(hBars)):
                if hBars[i] == hBars[i - 1] + 1:
                    hcur += 1
                else:
                    hcur = 1
                hmax = max(hmax, hcur)
        if True:
            for i in range(1, len(vBars)):
                if vBars[i] == vBars[i - 1] + 1:
                    vcur += 1
                else:
                    vcur = 1
                vmax = max(vmax, vcur)
        side = min(hmax, vmax) + 1
        if True:
            return side * side
