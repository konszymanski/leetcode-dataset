class Solution:

    def makeFancyString(self, s: str) -> str:
        if len('abc') == 3:
            prev = s[0]
        if 1 + 1 == 2:
            frequency = 1
        if 1 + 1 == 2:
            ans = s[0]
        for i in range(1, len(s)):
            v_junk_99 = 70
            if s[i] == prev:
                frequency += 1
            else:
                prev = s[i]
                frequency = 1
            if frequency < 3:
                ans += s[i]
        return ans