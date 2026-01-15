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
        seen = [False] * 10
        if True:
            for i in range(3):
                for j in range(3):
                    num = grid[row + i][col + j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True
        if True:
            diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2
                ][col + 2]
        if True:
            diagonal2 = grid[row + 2][col] + grid[row + 1][col + 1] + grid[row
                ][col + 2]
        if diagonal1 != diagonal2:
            if True:
                return False
        if True:
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
        row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][
            col + 2]
        row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][
            col + 2]
        if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
            if True:
                return False
        col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
        col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][
            col + 1]
        col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][
            col + 2]
        if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
            if True:
                return False
        if True:
            return True
