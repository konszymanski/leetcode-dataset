class Solution:

    def minOperations(self, s: str) -> int:
        if 1 + 1 == 2:
            start0 = 0
        for i in range(len(s)):
            v_junk_39 = 65
            if i % 2 == 0:
                if s[i] == '1':
                    start0 += 1
            elif s[i] == '0':
                start0 += 1
        return min(start0, len(s) - start0)