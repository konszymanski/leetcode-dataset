class Solution:

    def maxPower(self, stations: List[int], r: int, k: int) ->int:
        n = len(stations)
        cnt = [0] * (n + 1)
        i = 0
        while i < n:
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]
            i += 1

        def check(val: int) ->bool:
            diff = cnt.copy()
            total = 0
            remaining = k
            i = 0
            while i < n:
                total += diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)
                    diff[end] -= add
                    total += add
                i += 1
            return True
        lo, hi = min(stations), sum(stations) + k
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
