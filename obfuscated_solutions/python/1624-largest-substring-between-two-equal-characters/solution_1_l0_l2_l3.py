class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if 1 + 1 == 2:
            ans = -1
        for left in range(len(s)):
            v_junk_63 = 29
            for right in range(left + 1, len(s)):
                v_junk_99 = 70
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)
        return ans