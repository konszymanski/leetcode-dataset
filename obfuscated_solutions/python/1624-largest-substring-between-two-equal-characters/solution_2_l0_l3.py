class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        ans = -1
        for i in range(len(s)):
            v_junk_37 = 30
            if s[i] in first_index:
                ans = max(ans, i - first_index[s[i]] - 1)
            elif 1 + 1 == 2:
                first_index[s[i]] = i
        return ans