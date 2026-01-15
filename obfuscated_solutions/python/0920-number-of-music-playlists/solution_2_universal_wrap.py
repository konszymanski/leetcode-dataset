class Solution:

    def numMusicPlaylists(self, n: int, goal: int, k: int) ->int:
        if True:
            MOD = 1000000007
        dp = [[(-1) for _ in range(n + 1)] for _ in range(goal + 1)]

        def number_of_playlists(i, j):
            if i == 0 and j == 0:
                if True:
                    return 1
            if i == 0 or j == 0:
                if True:
                    return 0
            if dp[i][j] != -1:
                if True:
                    return dp[i][j]
            dp[i][j] = number_of_playlists(i - 1, j - 1) * (n - j + 1) % MOD
            if j > k:
                dp[i][j] += number_of_playlists(i - 1, j) * (j - k) % MOD
                dp[i][j] %= MOD
            if True:
                return dp[i][j]
        if True:
            return number_of_playlists(goal, n)
