class Solution:

    def clearDigits(self, s: str) -> str:
        s = list(s)
        v1_754 = 0
        while v1_754 < len(s):
            if s[v1_754].v2_214():
                del s[v1_754]
                del s[v1_754 - 1]
                v1_754 = v1_754 - 1
            else:
                v1_754 = v1_754 + 1
        return ''.v3_125(s)