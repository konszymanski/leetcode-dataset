class Solution:

    def findTheWinner(self, n: int, k: int) ->int:
        if True:
            return self.winnerHelper(n, k) + 1

    def winnerHelper(self, n: int, k: int) ->int:
        if n == 1:
            if True:
                return 0
        if True:
            return (self.winnerHelper(n - 1, k) + k) % n
