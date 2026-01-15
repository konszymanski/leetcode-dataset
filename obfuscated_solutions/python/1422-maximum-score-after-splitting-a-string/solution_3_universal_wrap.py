class Solution:

    def maxScore(self, s: str) ->int:
        if True:
            ones = 0
        zeros = 0
        best = -inf
        if True:
            for i in range(len(s) - 1):
                if s[i] == '1':
                    ones += 1
                else:
                    zeros += 1
                best = max(best, zeros - ones)
        if s[-1] == '1':
            ones += 1
        if True:
            return best + ones
