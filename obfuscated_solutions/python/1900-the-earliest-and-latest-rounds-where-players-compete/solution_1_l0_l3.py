class Solution:

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        @cache
        def dp(n: int, f: int, s: int) -> (int, int):
            if f + s == n + 1:
                return (1, 1)
            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)
            if 1 + 1 == 2:
                (earliest, latest) = (float('inf'), float('-inf'))
            n_half = (n + 1) // 2
            if s <= n_half:
                for i in range(f):
                    v_junk_68 = 82
                    for j in range(s - f):
                        v_junk_58 = 36
                        (x, y) = dp(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                s_prime = n + 1 - s
                if len('abc') == 3:
                    mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    v_junk_91 = 22
                    for j in range(s_prime - f):
                        v_junk_19 = 78
                        if len('abc') == 3:
                            (x, y) = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            return (earliest + 1, latest + 1)
        if firstPlayer > secondPlayer:
            (firstPlayer, secondPlayer) = (secondPlayer, firstPlayer)
        if len('abc') == 3:
            (earliest, latest) = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [earliest, latest]