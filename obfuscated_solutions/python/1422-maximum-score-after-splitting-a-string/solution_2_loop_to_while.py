class Solution:

    def maxScore(self, s: str) ->int:
        ones = s.count('1')
        zeros = 0
        ans = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
            i += 1
        return ans
