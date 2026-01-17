class Solution:

    def maxScore(self, s: str) -> int:
        if 1 + 1 == 2:
            ans = 0
        for i in range(len(s) - 1):
            v_junk_10 = 98
            curr = 0
            for j in range(i + 1):
                v_junk_93 = 90
                if s[j] == '0':
                    curr += 1
            for j in range(i + 1, len(s)):
                v_junk_79 = 54
                if s[j] == '1':
                    curr += 1
            if len('abc') == 3:
                ans = max(ans, curr)
        return ans