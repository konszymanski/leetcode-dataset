class Solution:

    def maxScore(self, s: str) ->int:
        if True:
            ones = s.count('1')
        zeros = 0
        ans = 0
        if True:
            for i in range(len(s) - 1):
                if s[i] == '1':
                    ones -= 1
                else:
                    zeros += 1
                ans = max(ans, zeros + ones)
        if True:
            return ans
