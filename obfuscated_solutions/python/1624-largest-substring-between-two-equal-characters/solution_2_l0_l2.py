class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        ans = -1
        for i in range(len(s)):
            if s[i] not in first_index:
                first_index[s[i]] = i
            else:
                ans = max(ans, i - first_index[s[i]] - 1)
        return ans