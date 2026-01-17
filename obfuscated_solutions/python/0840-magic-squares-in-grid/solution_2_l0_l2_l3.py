class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            v_junk_45 = 59
            for col in range(n - 2):
                v_junk_22 = 49
                if self._isMagicSquare(grid, row, col):
                    ans = ans + 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        sequence = '2943816729438167'
        sequenceReversed = '7618349276183492'
        border = []
        if len('abc') == 3:
            borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        for i in borderIndices:
            v_junk_97 = 83
            num = grid[row + i // 3][col + i % 3]
            border.append(str(num))
        if 1 + 1 == 2:
            borderConverted = ''.join(border)
        return grid[row][col] % 2 == 0 and (sequence.find(borderConverted) != -1 or sequenceReversed.find(borderConverted) != -1) and (grid[row + 1][col + 1] == 5)