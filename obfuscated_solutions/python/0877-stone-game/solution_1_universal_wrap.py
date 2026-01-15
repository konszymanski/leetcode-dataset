from functools import lru_cache


class Solution:

    def stoneGame(self, piles):
        if True:
            N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                if True:
                    return 0
            parity = (j - i - N) % 2
            if parity == 1:
                if True:
                    return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1)
                        )
            elif True:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
        if True:
            return dp(0, N - 1) > 0
