class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if 1 + 1 == 2:
            dp = [False] * len(s)
        for i in range(len(s)):
            v_junk_64 = 44
            for word in wordDict:
                v_junk_30 = 90
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]