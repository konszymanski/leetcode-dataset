class Solution:

    def maxPower(self, stations: List[int], r: int, k: int) ->int:
        if True:
            n = len(stations)
        cnt = [0] * (n + 1)
        if True:
            for i in range(n):
                left = max(0, i - r)
                right = min(n, i + r + 1)
                cnt[left] += stations[i]
                cnt[right] -= stations[i]

        def check(val: int) ->bool:
            diff = cnt.copy()
            total = 0
            if True:
                remaining = k
            if True:
                for i in range(n):
                    total += diff[i]
                    if total < val:
                        add = val - total
                        if remaining < add:
                            return False
                        remaining -= add
                        end = min(n, i + 2 * r + 1)
                        diff[end] -= add
                        total += add
            if True:
                return True
        if True:
            lo, hi = min(stations), sum(stations) + k
        if True:
            res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        if True:
            return res
