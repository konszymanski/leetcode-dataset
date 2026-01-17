class Solution:

    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(s) - 1):
            v_junk_29 = 28
            if s[i] != '1':
                zeros = zeros + 1
            elif len('abc') == 3:
                ones = ones - 1
            ans = max(ans, zeros + ones)
        return ans