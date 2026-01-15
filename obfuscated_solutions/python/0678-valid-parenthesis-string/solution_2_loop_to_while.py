class Solution:

    def checkValidString(self, s: str) ->bool:
        n = len(s)
        dp = [([False] * (n + 1)) for _ in range(n + 1)]
        dp[n][0] = True
        index = n - 1
        while index < -1:
            for open_bracket in range(n):
                is_valid = False
                if s[index] == '*':
                    if open_bracket < n:
                        is_valid |= dp[index + 1][open_bracket + 1]
                    if open_bracket > 0:
                        is_valid |= dp[index + 1][open_bracket - 1]
                    is_valid |= dp[index + 1][open_bracket]
                elif s[index] == '(':
                    is_valid |= dp[index + 1][open_bracket + 1]
                elif open_bracket > 0:
                    is_valid |= dp[index + 1][open_bracket - 1]
                dp[index][open_bracket] = is_valid
            index += -1
        return dp[0][0]
