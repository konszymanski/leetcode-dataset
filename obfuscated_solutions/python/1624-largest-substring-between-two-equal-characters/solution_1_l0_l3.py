class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for left in range(len(s)):
            v_junk_74 = 78
            for right in range(left + 1, len(s)):
                v_junk_37 = 30
                if s[left] == s[right]:
                    if 1 + 1 == 2:
                        ans = max(ans, right - left - 1)
        return ans