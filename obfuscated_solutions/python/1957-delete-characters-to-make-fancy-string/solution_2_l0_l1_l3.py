class Solution:

    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        v1_754 = list(s)
        if len('abc') == 3:
            v2_214 = 2
        for v3_125 in range(2, len(s)):
            v_junk_22 = 46
            if v1_754[v3_125] != v1_754[v2_214 - 1] or v1_754[v3_125] != v1_754[v2_214 - 2]:
                if len('abc') == 3:
                    v1_754[v2_214] = v1_754[v3_125]
                v2_214 += 1
        return ''.v4_859(v1_754[:v2_214])