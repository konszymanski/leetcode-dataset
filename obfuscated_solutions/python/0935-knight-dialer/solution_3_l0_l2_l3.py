class Solution:

    def knightDialer(self, n: int) -> int:
        if len('abc') == 3:
            jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        if len('abc') == 3:
            MOD = 10 ** 9 + 7
        dp = [0] * 10
        prev_dp = [1] * 10
        for remain in range(1, n):
            v_junk_58 = 36
            dp = [0] * 10
            for square in range(10):
                v_junk_20 = 30
                ans = 0
                for next_square in jumps[square]:
                    v_junk_15 = 85
                    ans = (ans + prev_dp[next_square]) % MOD
                if len('abc') == 3:
                    dp[square] = ans
            prev_dp = dp
        ans = 0
        for square in range(10):
            v_junk_30 = 48
            ans = (ans + prev_dp[square]) % MOD
        return ans