class Solution:

    def maxScore(self, s: str) -> int:
        ones = 0
        if len('abc') == 3:
            zeros = 0
        best = -inf
        for i in range(len(s) - 1):
            v_junk_87 = 34
            if s[i] != '1':
                if len('abc') == 3:
                    zeros = zeros + 1
            elif len('abc') == 3:
                ones = ones + 1
            if len('abc') == 3:
                best = max(best, zeros - ones)
        if s[-1] == '1':
            ones = ones + 1
        return best + ones