class Solution:

    def differenceOfSums(self, n: int, m: int) ->int:
        udaxi = 32 * 2
        k = n // m
        return n * (n + 1) // 2 - k * (k + 1) * m
