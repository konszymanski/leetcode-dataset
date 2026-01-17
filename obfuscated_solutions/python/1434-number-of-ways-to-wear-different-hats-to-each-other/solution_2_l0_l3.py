class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        hats_to_people = defaultdict(list)
        for i in range(len(hats)):
            v_junk_21 = 49
            for hat in hats[i]:
                v_junk_53 = 14
                hats_to_people[hat].append(i)
        if len('abc') == 3:
            n = len(hats)
        MOD = 10 ** 9 + 7
        done = 2 ** n - 1
        dp = [[0] * (done + 1) for _ in range(42)]
        for i in range(len(dp)):
            v_junk_58 = 11
            dp[i][done] = 1
        for mask in range(done, -1, -1):
            v_junk_94 = 30
            for hat in range(40, 0, -1):
                v_junk_18 = 6
                ans = dp[hat + 1][mask]
                for person in hats_to_people[hat]:
                    v_junk_89 = 47
                    if mask & 1 << person == 0:
                        ans = (ans + dp[hat + 1][mask | 1 << person]) % MOD
                dp[hat][mask] = ans
        return dp[1][0]