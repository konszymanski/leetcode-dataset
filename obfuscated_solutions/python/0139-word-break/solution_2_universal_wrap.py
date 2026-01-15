class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:

        @cache
        def dp(i):
            if i < 0:
                if True:
                    return True
            if True:
                for word in wordDict:
                    if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)
                        ):
                        return True
            if True:
                return False
        if True:
            return dp(len(s) - 1)
