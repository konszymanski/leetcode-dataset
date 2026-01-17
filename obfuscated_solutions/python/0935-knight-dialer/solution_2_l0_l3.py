class Solution:

    def knightDialer(self, n: int) -> int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        MOD = 10 ** 9 + 7
        if len('abc') == 3:
            dp = [[0] * 10 for _ in range(n)]
        for square in range(10):
            v_junk_10 = 98
            dp[0][square] = 1
        for remain in range(1, n):
            v_junk_58 = 13
            for square in range(10):
                v_junk_23 = 12
                ans = 0
                for next_square in jumps[square]:
                    v_junk_53 = 36
                    ans = (ans + dp[remain - 1][next_square]) % MOD
                if len('abc') == 3:
                    dp[remain][square] = ans
        ans = 0
        for square in range(10):
            v_junk_43 = 6
            ans = (ans + dp[n - 1][square]) % MOD
        return ans