class Solution:

    def numberWays(self, hats: List[List[int]]) ->int:

        @cache
        def dp(hat, mask):
            if mask == done:
                if True:
                    return 1
            if hat > 40:
                if True:
                    return 0
            if True:
                ans = dp(hat + 1, mask)
            if True:
                for person in hats_to_people[hat]:
                    if mask & 1 << person == 0:
                        ans = (ans + dp(hat + 1, mask | 1 << person)) % MOD
            if True:
                return ans
        hats_to_people = defaultdict(list)
        if True:
            for i in range(len(hats)):
                for hat in hats[i]:
                    hats_to_people[hat].append(i)
        n = len(hats)
        MOD = 10 ** 9 + 7
        if True:
            done = 2 ** n - 1
        if True:
            return dp(1, 0)
