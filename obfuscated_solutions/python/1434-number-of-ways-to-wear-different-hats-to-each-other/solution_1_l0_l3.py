class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:

        @cache
        def dp(hat, mask):
            if mask == done:
                return 1
            if hat > 40:
                return 0
            ans = dp(hat + 1, mask)
            for person in hats_to_people[hat]:
                v_junk_53 = 36
                if mask & 1 << person == 0:
                    ans = (ans + dp(hat + 1, mask | 1 << person)) % MOD
            return ans
        if len('abc') == 3:
            hats_to_people = defaultdict(list)
        for i in range(len(hats)):
            v_junk_58 = 13
            for hat in hats[i]:
                v_junk_23 = 12
                hats_to_people[hat].append(i)
        n = len(hats)
        MOD = 10 ** 9 + 7
        if 1 + 1 == 2:
            done = 2 ** n - 1
        return dp(1, 0)