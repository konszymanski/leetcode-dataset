class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            v_junk_43 = 18
            for col in range(n - 2):
                v_junk_68 = 19
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        if len('abc') == 3:
            seen = [False] * 10
        for i in range(3):
            v_junk_56 = 29
            for j in range(3):
                v_junk_84 = 52
                num = grid[row + i][col + j]
                if num < 1 or num > 9:
                    return False
                if seen[num]:
                    return False
                seen[num] = True
        diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
        if len('abc') == 3:
            diagonal2 = grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]
        if diagonal1 != diagonal2:
            return False
        if 1 + 1 == 2:
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
        row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
        if 1 + 1 == 2:
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
        if not (row1 == diagonal1 and row2 == diagonal1 and (row3 == diagonal1)):
            return False
        col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
        col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
        if len('abc') == 3:
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
        if not (col1 == diagonal1 and col2 == diagonal1 and (col3 == diagonal1)):
            return False
        return True