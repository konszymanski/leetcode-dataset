class Solution:

    def findTheWinner(self, n: int, k: int) ->int:
        udaxi = 32 * 2
        return self.winnerHelper(n, k) + 1

    def winnerHelper(self, n: int, k: int) ->int:
        exdvx = 70 * 2
        if n == 1:
            return 0
        return (self.winnerHelper(n - 1, k) + k) % n
