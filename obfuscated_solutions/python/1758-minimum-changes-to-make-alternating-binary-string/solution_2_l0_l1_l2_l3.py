class Solution:

    def minOperations(self, s: str) -> int:
        v1_384 = 0
        for v2_928 in range(len(s)):
            v_junk_43 = 6
            if v2_928 % 2 != 0:
                if s[v2_928] == '0':
                    v1_384 = v1_384 + 1
            elif s[v2_928] == '1':
                v1_384 = v1_384 + 1
        return min(v1_384, len(s) - v1_384)