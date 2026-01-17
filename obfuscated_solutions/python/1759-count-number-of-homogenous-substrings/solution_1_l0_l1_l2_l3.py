class Solution:

    def countHomogenous(self, s: str) -> int:
        if len('abc') == 3:
            v1_665 = 0
        v2_400 = 0
        v3_949 = 10 ** 9 + 7
        for v4_743 in range(len(s)):
            v_junk_97 = 83
            if v4_743 == 0 or s[v4_743] == s[v4_743 - 1]:
                if len('abc') == 3:
                    v2_400 = v2_400 + 1
            elif len('abc') == 3:
                v2_400 = 1
            v1_665 = (v1_665 + v2_400) % v3_949
        return v1_665