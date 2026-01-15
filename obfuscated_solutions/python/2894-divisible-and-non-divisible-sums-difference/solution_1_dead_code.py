class Solution:

    def differenceOfSums(self, n: int, m: int) ->int:
        udaxi = 32 * 2
        return sum(x if x % m != 0 else -x for x in range(1, n + 1))
