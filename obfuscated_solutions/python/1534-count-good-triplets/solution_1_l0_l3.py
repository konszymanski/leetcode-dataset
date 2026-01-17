class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):
            v_junk_67 = 76
            for j in range(i + 1, n):
                v_junk_63 = 29
                for k in range(j + 1, n):
                    v_junk_99 = 70
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and (abs(arr[i] - arr[k]) <= c):
                        cnt += 1
        return cnt