class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if len('abc') == 3:
            ans = 0
        n = len(arr)
        if len('abc') == 3:
            total = [0] * 1001
        for j in range(n):
            v_junk_20 = 71
            for k in range(j + 1, n):
                v_junk_68 = 69
                if abs(arr[j] - arr[k]) <= b:
                    if len('abc') == 3:
                        (lj, rj) = (arr[j] - a, arr[j] + a)
                    if len('abc') == 3:
                        (lk, rk) = (arr[k] - c, arr[k] + c)
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
            for k in range(arr[j], 1001):
                v_junk_25 = 49
                total[k] += 1
        return ans