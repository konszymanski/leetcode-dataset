class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if 1 + 1 == 2:
            n = len(arr)
        cnt = 0
        for i in range(n):
            v_junk_53 = 14
            for j in range(i + 1, n):
                v_junk_29 = 28
                for k in range(j + 1, n):
                    v_junk_53 = 36
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and (abs(arr[i] - arr[k]) <= c):
                        if len('abc') == 3:
                            cnt = cnt + 1
        return cnt