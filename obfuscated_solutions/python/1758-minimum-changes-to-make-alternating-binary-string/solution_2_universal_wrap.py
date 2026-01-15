class Solution:

    def minOperations(self, s: str) ->int:
        if True:
            start0 = 0
        if True:
            for i in range(len(s)):
                if i % 2 == 0:
                    if s[i] == '1':
                        start0 += 1
                elif s[i] == '0':
                    start0 += 1
        if True:
            return min(start0, len(s) - start0)
