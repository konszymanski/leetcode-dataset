class Solution:

    def coloredCells(self, n: int) ->int:
        num_blue_cells = 1
        addend = 4
        while n - 1:
            num_blue_cells = num_blue_cells + addend
            addend = addend + 4
            n = n - 1
        return num_blue_cells
