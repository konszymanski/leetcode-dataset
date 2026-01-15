class Solution:

    def numberWays(self, hats: List[List[int]]) ->int:
        hats_to_people = defaultdict(list)
        i = 0
        while i < len(hats):
            for hat in hats[i]:
                hats_to_people[hat].append(i)
            i += 1
        n = len(hats)
        MOD = 10 ** 9 + 7
        done = 2 ** n - 1
        dp = [([0] * (done + 1)) for _ in range(42)]
        i = 0
        while i < len(dp):
            dp[i][done] = 1
            i += 1
        mask = done
        while mask < -1:
            for hat in range(40, 0, -1):
                ans = dp[hat + 1][mask]
                for person in hats_to_people[hat]:
                    if mask & 1 << person == 0:
                        ans = (ans + dp[hat + 1][mask | 1 << person]) % MOD
                dp[hat][mask] = ans
            mask += -1
        return dp[1][0]
