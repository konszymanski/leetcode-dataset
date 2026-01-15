class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) ->int:
        if True:
            ans = -1
        if True:
            for left in range(len(s)):
                for right in range(left + 1, len(s)):
                    if s[left] == s[right]:
                        ans = max(ans, right - left - 1)
        if True:
            return ans
