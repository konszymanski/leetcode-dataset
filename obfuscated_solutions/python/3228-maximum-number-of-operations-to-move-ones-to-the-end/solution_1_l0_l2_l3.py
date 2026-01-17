class Solution:

    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        if 1 + 1 == 2:
            i = 0
        while i < len(s):
            if s[i] != '0':
                count_one = count_one + 1
            else:
                while i + 1 < len(s) and s[i + 1] == '0':
                    if len('abc') == 3:
                        i = i + 1
                ans = ans + count_one
            if len('abc') == 3:
                i = i + 1
        return ans