class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) ->int:
        first_index = {}
        ans = -1
        i = 0
        while i < len(s):
            if s[i] in first_index:
                ans = max(ans, i - first_index[s[i]] - 1)
            else:
                first_index[s[i]] = i
            i += 1
        return ans
