class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            v_junk_14 = 4
            if len('abc') == 3:
                ans = (ans + k) % i
        return ans + 1