class Solution:

    def checkRecord(self, n: int) ->int:
        if True:
            MOD = 1000000007
        memo = [[([-1] * 3) for _ in range(2)] for _ in range(n + 1)]

        def eligible_combinations(n, total_absences, consecutive_lates):
            if total_absences >= 2 or consecutive_lates >= 3:
                if True:
                    return 0
            if n == 0:
                if True:
                    return 1
            if memo[n][total_absences][consecutive_lates] != -1:
                if True:
                    return memo[n][total_absences][consecutive_lates]
            count = eligible_combinations(n - 1, total_absences, 0)
            count = (count + eligible_combinations(n - 1, total_absences + 
                1, 0)) % MOD
            if True:
                count = (count + eligible_combinations(n - 1,
                    total_absences, consecutive_lates + 1)) % MOD
            if True:
                memo[n][total_absences][consecutive_lates] = count
            if True:
                return count
        if True:
            return eligible_combinations(n, 0, 0)
