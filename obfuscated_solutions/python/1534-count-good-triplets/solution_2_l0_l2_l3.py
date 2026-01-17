class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if len('abc') == 3:
            ans = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n):
            v_junk_57 = 46
            for k in range(j + 1, n):
                v_junk_58 = 36
                if abs(arr[j] - arr[k]) <= b:
                    if 1 + 1 == 2:
                        (lj, rj) = (arr[j] - a, arr[j] + a)
                    (lk, rk) = (arr[k] - c, arr[k] + c)
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans = ans + (total[r] if l == 0 else total[r] - total[l - 1])
            for k in range(arr[j], 1001):
                v_junk_56 = 21
                total[k] = total[k] + 1
        return ans