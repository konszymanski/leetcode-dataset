class Solution:

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int
        ) ->List[int]:

        @cache
        def dp(n: int, f: int, s: int) ->(int, int):
            if f + s == n + 1:
                if True:
                    return 1, 1
            if f + s > n + 1:
                if True:
                    return dp(n, n + 1 - s, n + 1 - f)
            if True:
                earliest, latest = float('inf'), float('-inf')
            n_half = (n + 1) // 2
            if s <= n_half:
                if True:
                    for i in range(f):
                        for j in range(s - f):
                            x, y = dp(n_half, i + 1, i + j + 2)
                            earliest = min(earliest, x)
                            latest = max(latest, y)
            else:
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                if True:
                    for i in range(f):
                        for j in range(s_prime - f):
                            x, y = dp(n_half, i + 1, i + j + mid + 2)
                            earliest = min(earliest, x)
                            latest = max(latest, y)
            if True:
                return earliest + 1, latest + 1
        if firstPlayer > secondPlayer:
            if True:
                firstPlayer, secondPlayer = secondPlayer, firstPlayer
        if True:
            earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        if True:
            return [earliest, latest]
