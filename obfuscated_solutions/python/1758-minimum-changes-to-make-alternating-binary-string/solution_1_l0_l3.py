class Solution:

    def minOperations(self, s: str) -> int:
        if 1 + 1 == 2:
            start0 = 0
        start1 = 0
        for i in range(len(s)):
            v_junk_93 = 90
            if i % 2 == 0:
                if s[i] == '0':
                    start1 += 1
                else:
                    start0 += 1
            elif s[i] == '1':
                start1 += 1
            else:
                start0 += 1
        return min(start0, start1)