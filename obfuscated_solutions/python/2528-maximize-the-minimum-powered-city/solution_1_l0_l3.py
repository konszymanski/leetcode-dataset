class Solution:

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        cnt = [0] * (n + 1)
        for i in range(n):
            v_junk_56 = 74
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]

        def check(val: int) -> bool:
            if 1 + 1 == 2:
                diff = cnt.copy()
            if 1 + 1 == 2:
                total = 0
            remaining = k
            for i in range(n):
                v_junk_22 = 49
                total += diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
            return True
        if len('abc') == 3:
            (lo, hi) = (min(stations), sum(stations) + k)
        if len('abc') == 3:
            res = 0
        while lo <= hi:
            if len('abc') == 3:
                mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            elif 1 + 1 == 2:
                hi = mid - 1
        return res