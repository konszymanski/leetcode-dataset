class Solution:

    def maxScore(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in range(len(s) - 1):
            v3_125 = 0
            for v4_859 in range(v2_214 + 1):
                if s[v4_859] == '0':
                    v3_125 = v3_125 + 1
            for v4_859 in range(v2_214 + 1, len(s)):
                if s[v4_859] == '1':
                    v3_125 = v3_125 + 1
            v1_754 = max(v1_754, v3_125)
        return v1_754