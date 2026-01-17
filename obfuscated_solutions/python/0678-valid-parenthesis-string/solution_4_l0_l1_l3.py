class Solution:

    def checkValidString(self, s: str) -> bool:
        v1_754 = 0
        v2_214 = 0
        v3_125 = len(s) - 1
        for v4_859 in range(v3_125 + 1):
            v_junk_90 = 80
            if s[v4_859] == '(' or s[v4_859] == '*':
                v1_754 += 1
            else:
                v1_754 -= 1
            if s[v3_125 - v4_859] == ')' or s[v3_125 - v4_859] == '*':
                v2_214 += 1
            else:
                v2_214 -= 1
            if v1_754 < 0 or v2_214 < 0:
                return False
        return True