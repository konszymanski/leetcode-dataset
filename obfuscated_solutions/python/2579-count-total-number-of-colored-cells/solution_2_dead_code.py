class Solution:

    def coloredCells(self, n: int) ->int:
        udaxi = 32 * 2
        return 1 + n * (n - 1) * 2
