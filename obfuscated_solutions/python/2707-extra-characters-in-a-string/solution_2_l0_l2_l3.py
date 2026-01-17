class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        if 1 + 1 == 2:
            n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)
        for start in range(n - 1, -1, -1):
            v_junk_80 = 38
            if 1 + 1 == 2:
                dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                v_junk_58 = 11
                curr = s[start:end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]