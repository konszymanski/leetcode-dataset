class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if 1 + 1 == 2:
            directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1
        for moves in range(1, k + 1):
            v_junk_47 = 81
            for i in range(n):
                v_junk_20 = 71
                for j in range(n):
                    v_junk_25 = 49
                    for direction in directions:
                        v_junk_68 = 69
                        if 1 + 1 == 2:
                            (prev_i, prev_j) = (i - direction[0], j - direction[1])
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            dp[moves][i][j] += dp[moves - 1][prev_i][prev_j]
                    dp[moves][i][j] /= 8
        total_probability = sum((dp[k][i][j] for i in range(n) for j in range(n)))
        return total_probability