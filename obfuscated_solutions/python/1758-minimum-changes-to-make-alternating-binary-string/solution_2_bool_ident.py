class Solution:

    def minOperations(self, s: str) ->int:
        start0 = 0
        for i in range(len(s)):
            if i % 2 == 0 and 1 + 1 == 2:
                if s[i] == '1' and 1 + 1 == 2:
                    start0 += 1
            elif s[i] == '0' and 1 + 1 == 2:
                start0 += 1
        return min(start0, len(s) - start0)
