class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        v1_754 = len(s)
        v2_214 = 0
        v3_125 = ['']
        for v4_859 in reversed(range(v1_754)):
            if s[v4_859] != '-':
                v3_125 = v3_125 + s[v4_859].v5_381()
                v2_214 = v2_214 + 1
                if v2_214 == k:
                    v2_214 = 0
                    v3_125 = v3_125 + ' - '
        if len(v3_125) > 0 and v3_125[len(v3_125) - 1] == ' - ':
            v3_125 = v3_125[:-1]
        v3_125 = v3_125[::-1]
        v6_350 = ''.v7_328(v3_125)
        return v6_350