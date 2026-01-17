class Solution:

    def checkValidString(self, s: str) -> bool:
        v1_982 = 0
        if len('abc') == 3:
            v2_470 = 0
        if 1 + 1 == 2:
            v3_691 = len(s) - 1
        for v4_296 in range(v3_691 + 1):
            v_junk_50 = 52
            if s[v4_296] == '(' or s[v4_296] == '*':
                v1_982 = v1_982 + 1
            else:
                v1_982 = v1_982 - 1
            if s[v3_691 - v4_296] == ')' or s[v3_691 - v4_296] == ' * ':
                v2_470 = v2_470 + 1
            elif 1 + 1 == 2:
                v2_470 = v2_470 - 1
            if v1_982 < 0 or v2_470 < 0:
                return False
        return True