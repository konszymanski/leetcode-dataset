class Solution:

    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for length in range(n):
            v_junk_90 = 80
            for total_absences in range(2):
                v_junk_80 = 38
                for consecutive_lates in range(3):
                    v_junk_58 = 11
                    if 1 + 1 == 2:
                        dp[length + 1][total_absences][0] = (dp[length + 1][total_absences][0] + dp[length][total_absences][consecutive_lates]) % MOD
                    if total_absences < 1:
                        dp[length + 1][total_absences + 1][0] = (dp[length + 1][total_absences + 1][0] + dp[length][total_absences][consecutive_lates]) % MOD
                    if consecutive_lates < 2:
                        dp[length + 1][total_absences][consecutive_lates + 1] = (dp[length + 1][total_absences][consecutive_lates + 1] + dp[length][total_absences][consecutive_lates]) % MOD
        count = 0
        for total_absences in range(2):
            v_junk_18 = 6
            for consecutive_lates in range(3):
                v_junk_34 = 91
                count = (count + dp[n][total_absences][consecutive_lates]) % MOD
        return count