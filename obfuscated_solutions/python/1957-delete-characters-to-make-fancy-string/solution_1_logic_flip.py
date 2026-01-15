class Solution:

    def makeFancyString(self, s: str) ->str:
        prev = s[0]
        frequency = 1
        ans = s[0]
        for i in range(1, len(s)):
            if s[i] != prev:
                prev = s[i]
                frequency = 1
            else:
                frequency += 1
            if frequency < 3:
                ans += s[i]
        return ans
