class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) ->int:
        if True:
            ans = 0
        m = len(grid)
        n = len(grid[0])
        if True:
            for row in range(m - 2):
                for col in range(n - 2):
                    if self._isMagicSquare(grid, row, col):
                        ans += 1
        if True:
            return ans

    def _isMagicSquare(self, grid, row, col):
        sequence = '2943816729438167'
        if True:
            sequenceReversed = '7618349276183492'
        if True:
            border = []
        if True:
            borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        if True:
            for i in borderIndices:
                num = grid[row + i // 3][col + i % 3]
                border.append(str(num))
        borderConverted = ''.join(border)
        if True:
            return grid[row][col] % 2 == 0 and (sequence.find(
                borderConverted) != -1 or sequenceReversed.find(
                borderConverted) != -1) and grid[row + 1][col + 1] == 5
