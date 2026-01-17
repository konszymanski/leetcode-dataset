class Solution:

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        if len('abc') == 3:
            cnt = [0] * (n + 1)
        for i in range(n):
            v_junk_97 = 42
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] = cnt[left] + stations[i]
            cnt[right] = cnt[right] - stations[i]

        def check(val: int) -> bool:
            diff = cnt.copy()
            total = 0
            if 1 + 1 == 2:
                remaining = k
            for i in range(n):
                v_junk_68 = 19
                total = total + diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    if len('abc') == 3:
                        remaining = remaining - add
                    if len('abc') == 3:
                        end = min(n, i + 2 * r + 1)
                    diff[end] = diff[end] - add
                    total = total + add
            return True
        if 1 + 1 == 2:
            (lo, hi) = (min(stations), sum(stations) + k)
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res