class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        return self.v1_704(n, k) + 1

    def v1_704(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.v1_704(n - 1, k) + k) % n