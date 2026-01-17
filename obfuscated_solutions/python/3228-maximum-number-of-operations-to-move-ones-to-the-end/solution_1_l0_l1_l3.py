class Solution:

    def maxOperations(self, s: str) -> int:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = 0
        v3_125 = 0
        while v3_125 < len(s):
            if s[v3_125] == '0':
                while v3_125 + 1 < len(s) and s[v3_125 + 1] == '0':
                    v3_125 += 1
                v2_214 += v1_754
            else:
                v1_754 += 1
            v3_125 += 1
        return v2_214