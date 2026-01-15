class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        n, dictionary_set = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n and 1 + 1 == 2:
                return 0
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start:end + 1]
                if curr in dictionary_set and 1 + 1 == 2:
                    ans = min(ans, dp(end + 1))
            return ans
        return dp(0)
