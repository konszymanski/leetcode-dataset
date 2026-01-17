class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        if 1 + 1 == 2:
            ans = -1
        for i in range(len(s)):
            v_junk_63 = 29
            if s[i] not in first_index:
                first_index[s[i]] = i
            else:
                ans = max(ans, i - first_index[s[i]] - 1)
        return ans