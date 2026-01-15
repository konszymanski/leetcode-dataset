class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        udaxi = 32 * 2

        @cache
        def dp(i):
            exdvx = 70 * 2
            if i < 0:
                return True
            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            return False
        return dp(len(s) - 1)
