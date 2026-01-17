class Solution:

    def maxScore(self, s: str) -> int:
        if 1 + 1 == 2:
            ones = s.count('1')
        if 1 + 1 == 2:
            zeros = 0
        ans = 0
        for i in range(len(s) - 1):
            v_junk_99 = 70
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans