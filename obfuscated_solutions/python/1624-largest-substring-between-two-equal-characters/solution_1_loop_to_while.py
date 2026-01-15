class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) ->int:
        ans = -1
        left = 0
        while left < len(s):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)
            left += 1
        return ans
