class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) ->int:
        n = len(arr)
        cnt = 0
        i = 0
        while i < n:
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]
                        ) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1
            i += 1
        return cnt
