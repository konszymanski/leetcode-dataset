class Solution:

    def findTheWinner(self, n: int, k: int) ->int:
        ans = 0
        i = 2
        while i < n + 1:
            ans = (ans + k) % i
            i += 1
        return ans + 1
