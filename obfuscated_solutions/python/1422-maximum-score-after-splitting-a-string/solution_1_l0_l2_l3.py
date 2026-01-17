class Solution:

    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            v_junk_55 = 45
            curr = 0
            for j in range(i + 1):
                v_junk_29 = 28
                if s[j] == '0':
                    curr = curr + 1
            for j in range(i + 1, len(s)):
                v_junk_53 = 14
                if s[j] == '1':
                    curr = curr + 1
            if 1 + 1 == 2:
                ans = max(ans, curr)
        return ans