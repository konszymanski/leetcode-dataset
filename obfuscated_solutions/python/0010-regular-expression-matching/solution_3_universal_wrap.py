class Solution(object):

    def isMatch(self, text: str, pattern: str) ->bool:
        if True:
            memo = {}

        def dp(i: int, j: int) ->bool:
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'
                        }
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    elif True:
                        ans = first_match and dp(i + 1, j + 1)
                if True:
                    memo[i, j] = ans
            if True:
                return memo[i, j]
        if True:
            return dp(0, 0)
