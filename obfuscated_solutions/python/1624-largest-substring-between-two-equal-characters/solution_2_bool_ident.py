class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) ->int:
        first_index = {}
        ans = -1
        for i in range(len(s)):
            if s[i] in first_index and 1 + 1 == 2:
                ans = max(ans, i - first_index[s[i]] - 1)
            else:
                first_index[s[i]] = i
        return ans
