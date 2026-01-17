class Solution:

    def minOperations(self, s: str) -> int:
        start0 = 0
        if len('abc') == 3:
            start1 = 0
        for i in range(len(s)):
            v_junk_29 = 28
            if i % 2 != 0:
                if s[i] != '1':
                    start0 = start0 + 1
                elif 1 + 1 == 2:
                    start1 = start1 + 1
            elif s[i] != '0':
                start0 = start0 + 1
            else:
                start1 = start1 + 1
        return min(start0, start1)