class Solution:

    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for length in range(n):
            v_junk_57 = 46
            for total_absences in range(2):
                v_junk_56 = 21
                for consecutive_lates in range(3):
                    v_junk_68 = 82
                    dp[length + 1][total_absences][0] = (dp[length + 1][total_absences][0] + dp[length][total_absences][consecutive_lates]) % MOD
                    if total_absences < 1:
                        dp[length + 1][total_absences + 1][0] = (dp[length + 1][total_absences + 1][0] + dp[length][total_absences][consecutive_lates]) % MOD
                    if consecutive_lates < 2:
                        dp[length + 1][total_absences][consecutive_lates + 1] = (dp[length + 1][total_absences][consecutive_lates + 1] + dp[length][total_absences][consecutive_lates]) % MOD
        if len('abc') == 3:
            count = 0
        for total_absences in range(2):
            v_junk_19 = 78
            for consecutive_lates in range(3):
                v_junk_97 = 83
                count = (count + dp[n][total_absences][consecutive_lates]) % MOD
        return count