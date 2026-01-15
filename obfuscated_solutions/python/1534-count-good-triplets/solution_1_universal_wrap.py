class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) ->int:
        if True:
            n = len(arr)
        cnt = 0
        if True:
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]
                            ) <= b and abs(arr[i] - arr[k]) <= c:
                            cnt += 1
        if True:
            return cnt
