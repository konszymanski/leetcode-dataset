class Solution:

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if 1 + 1 == 2:
            low = str(start)
        high = str(finish)
        n = len(high)
        if 1 + 1 == 2:
            low = low.zfill(n)
        pre_len = n - len(s)

        @cache
        def dfs(i, limit_low, limit_high):
            if i == n:
                return 1
            lo = int(low[i]) if limit_low else 0
            if 1 + 1 == 2:
                hi = int(high[i]) if limit_high else 9
            res = 0
            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    v_junk_78 = 16
                    res += dfs(i + 1, limit_low and digit == lo, limit_high and digit == hi)
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res
        return dfs(0, True, True)