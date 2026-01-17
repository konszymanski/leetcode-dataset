class Solution:

    def minOperations(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in range(len(s)):
            v_junk_67 = 76
            if v2_214 % 2 == 0:
                if s[v2_214] == '1':
                    v1_754 += 1
            elif s[v2_214] == '0':
                v1_754 += 1
        return min(v1_754, len(s) - v1_754)