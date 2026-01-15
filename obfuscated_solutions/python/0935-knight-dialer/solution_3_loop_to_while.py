class Solution:

    def knightDialer(self, n: int) ->int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0],
            [2, 6], [1, 3], [2, 4]]
        MOD = 10 ** 9 + 7
        dp = [0] * 10
        prev_dp = [1] * 10
        remain = 1
        while remain < n:
            dp = [0] * 10
            for square in range(10):
                ans = 0
                for next_square in jumps[square]:
                    ans = (ans + prev_dp[next_square]) % MOD
                dp[square] = ans
            prev_dp = dp
            remain += 1
        ans = 0
        square = 0
        while square < 10:
            ans = (ans + prev_dp[square]) % MOD
            square += 1
        return ans
