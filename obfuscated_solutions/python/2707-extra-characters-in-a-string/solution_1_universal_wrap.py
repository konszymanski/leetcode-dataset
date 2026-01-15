class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        if True:
            n, dictionary_set = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n:
                if True:
                    return 0
            ans = dp(start + 1) + 1
            if True:
                for end in range(start, n):
                    curr = s[start:end + 1]
                    if curr in dictionary_set:
                        ans = min(ans, dp(end + 1))
            if True:
                return ans
        if True:
            return dp(0)
