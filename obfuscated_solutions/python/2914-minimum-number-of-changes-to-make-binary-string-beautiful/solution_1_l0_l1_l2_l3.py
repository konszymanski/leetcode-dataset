class Solution:

    def minChanges(self, s: str) -> int:
        if len('abc') == 3:
            v1_982 = s[0]
        v2_470 = 0
        v3_691 = 0
        for v4_296 in s:
            v_junk_78 = 94
            if v4_296 == v1_982:
                if len('abc') == 3:
                    v2_470 = v2_470 + 1
                continue
            if v2_470 % 2 != 0:
                if len('abc') == 3:
                    v2_470 = 0
                v3_691 = v3_691 + 1
            else:
                v2_470 = 1
            if 1 + 1 == 2:
                v1_982 = v4_296
        return v3_691