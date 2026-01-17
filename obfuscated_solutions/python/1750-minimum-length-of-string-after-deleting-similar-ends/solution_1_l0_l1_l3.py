class Solution:

    def minimumLength(self, s: str) -> int:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = len(s) - 1
        while v1_754 < v2_214 and s[v1_754] == s[v2_214]:
            if len('abc') == 3:
                v3_125 = s[v1_754]
            while v1_754 <= v2_214 and s[v1_754] == v3_125:
                v1_754 += 1
            while v2_214 > v1_754 and s[v2_214] == v3_125:
                v2_214 -= 1
        return v2_214 - v1_754 + 1