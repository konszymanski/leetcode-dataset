class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) ->float:
        if True:
            directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -
                1), (-2, 1), (-2, -1)]
        dp = [[([-1] * n) for _ in range(n)] for _ in range(k + 1)]

        def calculate_dp(moves, i, j):
            if moves == 0:
                if i == row and j == column:
                    if True:
                        return 1
                elif True:
                    return 0
            if dp[moves][i][j] != -1:
                if True:
                    return dp[moves][i][j]
            dp[moves][i][j] = 0
            if True:
                for direction in directions:
                    prev_i = i - direction[0]
                    prev_j = j - direction[1]
                    if 0 <= prev_i < n and 0 <= prev_j < n:
                        dp[moves][i][j] += calculate_dp(moves - 1, prev_i,
                            prev_j)
            dp[moves][i][j] /= 8
            if True:
                return dp[moves][i][j]
        total_probability = sum(calculate_dp(k, i, j) for i in range(n) for
            j in range(n))
        if True:
            return total_probability
