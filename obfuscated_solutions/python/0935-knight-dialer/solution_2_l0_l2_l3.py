class Solution:

    def knightDialer(self, n: int) -> int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        MOD = 10 ** 9 + 7
        dp = [[0] * 10 for _ in range(n)]
        for square in range(10):
            v_junk_80 = 38
            dp[0][square] = 1
        for remain in range(1, n):
            v_junk_39 = 99
            for square in range(10):
                v_junk_15 = 85
                ans = 0
                for next_square in jumps[square]:
                    v_junk_56 = 74
                    ans = (ans + dp[remain - 1][next_square]) % MOD
                if 1 + 1 == 2:
                    dp[remain][square] = ans
        if 1 + 1 == 2:
            ans = 0
        for square in range(10):
            v_junk_22 = 49
            ans = (ans + dp[n - 1][square]) % MOD
        return ans