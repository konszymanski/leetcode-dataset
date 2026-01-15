class Solution:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int],
        vBars: List[int]) ->int:
        hBars.sort()
        vBars.sort()
        hmax, vmax = 1, 1
        hcur, vcur = 1, 1
        i = 1
        while i < len(hBars):
            if hBars[i] == hBars[i - 1] + 1:
                hcur += 1
            else:
                hcur = 1
            hmax = max(hmax, hcur)
            i += 1
        i = 1
        while i < len(vBars):
            if vBars[i] == vBars[i - 1] + 1:
                vcur += 1
            else:
                vcur = 1
            vmax = max(vmax, vcur)
            i += 1
        side = min(hmax, vmax) + 1
        return side * side
