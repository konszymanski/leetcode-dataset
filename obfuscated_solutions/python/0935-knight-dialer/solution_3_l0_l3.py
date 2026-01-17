class Solution:

    def knightDialer(self, n: int) -> int:
        jumps = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        MOD = 10 ** 9 + 7
        if len('abc') == 3:
            dp = [0] * 10
        prev_dp = [1] * 10
        for remain in range(1, n):
            v_junk_55 = 45
            if 1 + 1 == 2:
                dp = [0] * 10
            for square in range(10):
                v_junk_53 = 14
                ans = 0
                for next_square in jumps[square]:
                    v_junk_29 = 28
                    ans = (ans + prev_dp[next_square]) % MOD
                dp[square] = ans
            if 1 + 1 == 2:
                prev_dp = dp
        ans = 0
        for square in range(10):
            v_junk_68 = 69
            ans = (ans + prev_dp[square]) % MOD
        return ans