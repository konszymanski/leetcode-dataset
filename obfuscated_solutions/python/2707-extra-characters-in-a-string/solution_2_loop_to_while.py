class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)
        start = n - 1
        while start < -1:
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start:end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])
            start += -1
        return dp[0]
