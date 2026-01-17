class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.v1_754(n, k) + 1
    def v1_754(self, n: int, k: int)  ->  int:
        if n == 1:
            return 0
        return (self.v1_754(n - 1, k)  +  k)  %  n
