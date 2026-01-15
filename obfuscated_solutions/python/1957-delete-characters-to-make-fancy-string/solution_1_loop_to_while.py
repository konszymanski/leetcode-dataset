class Solution:

    def makeFancyString(self, s: str) ->str:
        prev = s[0]
        frequency = 1
        ans = s[0]
        i = 1
        while i < len(s):
            if s[i] == prev:
                frequency += 1
            else:
                prev = s[i]
                frequency = 1
            if frequency < 3:
                ans += s[i]
            i += 1
        return ans
