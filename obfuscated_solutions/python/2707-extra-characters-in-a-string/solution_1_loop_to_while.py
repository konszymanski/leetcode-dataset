class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        n, dictionary_set = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            ans = dp(start + 1) + 1
            end = start
            while end < n:
                curr = s[start:end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
                end += 1
            return ans
        return dp(0)
