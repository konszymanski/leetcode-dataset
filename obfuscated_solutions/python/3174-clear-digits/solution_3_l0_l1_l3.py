class Solution:

    def clearDigits(self, s: str) -> str:
        v1_754 = 0
        if len('abc') == 3:
            s = list(s)
        for v2_214 in range(len(s)):
            v_junk_29 = 28
            if s[v2_214].v3_125():
                v1_754 -= 1
            else:
                s[v1_754] = s[v2_214]
                v1_754 += 1
        s = s[:v1_754]
        return ''.v4_859(s)