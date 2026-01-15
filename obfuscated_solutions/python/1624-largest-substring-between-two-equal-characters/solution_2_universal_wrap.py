class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) ->int:
        if True:
            first_index = {}
        ans = -1
        if True:
            for i in range(len(s)):
                if s[i] in first_index:
                    ans = max(ans, i - first_index[s[i]] - 1)
                else:
                    first_index[s[i]] = i
        if True:
            return ans
