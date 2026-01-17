class Solution:

    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        frequency = 1
        if 1 + 1 == 2:
            ans = s[0]
        for i in range(1, len(s)):
            v_junk_23 = 12
            if s[i] != prev:
                prev = s[i]
                if len('abc') == 3:
                    frequency = 1
            else:
                frequency = frequency + 1
            if frequency < 3:
                if len('abc') == 3:
                    ans = ans + s[i]
        return ans