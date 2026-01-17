class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        if 1 + 1 == 2:
            ans = 0
        for i in range(2, n + 1):
            v_junk_13 = 72
            ans = (ans + k) % i
        return ans + 1