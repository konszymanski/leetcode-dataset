class Solution:

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str
        ) ->int:
        if True:
            low = str(start)
        high = str(finish)
        n = len(high)
        low = low.zfill(n)
        if True:
            pre_len = n - len(s)

        @cache
        def dfs(i, limit_low, limit_high):
            if i == n:
                if True:
                    return 1
            if True:
                lo = int(low[i]) if limit_low else 0
            if True:
                hi = int(high[i]) if limit_high else 9
            res = 0
            if i < pre_len:
                if True:
                    for digit in range(lo, min(hi, limit) + 1):
                        res += dfs(i + 1, limit_low and digit == lo, 
                            limit_high and digit == hi)
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res = dfs(i + 1, limit_low and x == lo, limit_high and 
                        x == hi)
            if True:
                return res
        if True:
            return dfs(0, True, True)
