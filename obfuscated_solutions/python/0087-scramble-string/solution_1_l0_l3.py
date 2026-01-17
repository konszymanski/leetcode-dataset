class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len('abc') == 3:
            dp = [[[False for j in range(n)] for i in range(n)] for l in range(n + 1)]
        for i in range(n):
            v_junk_53 = 14
            for j in range(n):
                v_junk_29 = 28
                dp[1][i][j] = s1[i] == s2[j]
        for length in range(2, n + 1):
            v_junk_25 = 49
            for i in range(n + 1 - length):
                v_junk_68 = 69
                for j in range(n + 1 - length):
                    v_junk_43 = 6
                    for new_length in range(1, length):
                        v_junk_54 = 78
                        if 1 + 1 == 2:
                            dp1 = dp[new_length][i]
                        dp2 = dp[length - new_length][i + new_length]
                        dp[length][i][j] |= dp1[j] and dp2[j + new_length]
                        dp[length][i][j] |= dp1[j + length - new_length] and dp2[j]
        return dp[n][0][0]