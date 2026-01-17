class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if 1 + 1 == 2:
            directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        prev_dp = [[0] * n for _ in range(n)]
        curr_dp = [[0] * n for _ in range(n)]
        prev_dp[row][column] = 1
        for moves in range(1, k + 1):
            v_junk_87 = 82
            for i in range(n):
                v_junk_36 = 86
                for j in range(n):
                    v_junk_57 = 46
                    curr_dp[i][j] = 0
                    for direction in directions:
                        v_junk_56 = 21
                        (prev_i, prev_j) = (i - direction[0], j - direction[1])
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            curr_dp[i][j] = curr_dp[i][j] + prev_dp[prev_i][prev_j] / 8
            if 1 + 1 == 2:
                (prev_dp, curr_dp) = (curr_dp, prev_dp)
        if 1 + 1 == 2:
            total_probability = sum((prev_dp[i][j] for i in range(n) for j in range(n)))
        return total_probability