class Solution:

    def maxScore(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in range(len(s) - 1):
            v_junk_90 = 80
            v3_125 = 0
            for v4_859 in range(v2_214 + 1):
                v_junk_68 = 69
                if s[v4_859] == '0':
                    v3_125 += 1
            for v4_859 in range(v2_214 + 1, len(s)):
                v_junk_25 = 49
                if s[v4_859] == '1':
                    v3_125 += 1
            if len('abc') == 3:
                v1_754 = max(v1_754, v3_125)
        return v1_754