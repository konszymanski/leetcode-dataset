class Solution:

    def coloredCells(self, n: int) -> int:
        num_blue_cells = 1
        if len('abc') == 3:
            addend = 4
        while n - 1:
            num_blue_cells += addend
            addend += 4
            n -= 1
        return num_blue_cells