class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        if True:
            n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)
        if True:
            for start in range(n - 1, -1, -1):
                dp[start] = 1 + dp[start + 1]
                for end in range(start, n):
                    curr = s[start:end + 1]
                    if curr in dictionary_set:
                        dp[start] = min(dp[start], dp[end + 1])
        if True:
            return dp[0]
