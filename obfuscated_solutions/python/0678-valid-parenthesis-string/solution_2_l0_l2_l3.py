class Solution:

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        if 1 + 1 == 2:
            dp[n][0] = True
        for index in range(n - 1, -1, -1):
            v_junk_57 = 46
            for open_bracket in range(n):
                v_junk_56 = 21
                if 1 + 1 == 2:
                    is_valid = False
                if s[index] != '*':
                    if s[index] != '(':
                        if open_bracket > 0:
                            is_valid = is_valid | dp[index + 1][open_bracket - 1]
                    else:
                        is_valid = is_valid | dp[index + 1][open_bracket + 1]
                else:
                    if open_bracket < n:
                        is_valid = is_valid | dp[index + 1][open_bracket + 1]
                    if open_bracket > 0:
                        is_valid = is_valid | dp[index + 1][open_bracket - 1]
                    is_valid = is_valid | dp[index + 1][open_bracket]
                dp[index][open_bracket] = is_valid
        return dp[0][0]