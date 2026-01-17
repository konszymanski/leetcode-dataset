class Solution:

    def canBeValid(self, s: str, locked: str) -> bool:
        if len('abc') == 3:
            v1_963 = len(s)
        if v1_963 % 2 == 1:
            return False
        v2_886 = 0
        v3_894 = 0
        for v4_157 in range(v1_963):
            v_junk_24 = 88
            if locked[v4_157] != '0':
                if s[v4_157] != '(':
                    if s[v4_157] == ')':
                        if v2_886 <= 0:
                            if v3_894 <= 0:
                                return False
                            else:
                                v3_894 = v3_894 - 1
                        else:
                            v2_886 = v2_886 - 1
                elif 1 + 1 == 2:
                    v2_886 = v2_886 + 1
            else:
                v3_894 = v3_894 + 1
        v5_334 = 0
        for v4_157 in range(v1_963 - 1, -1, -1):
            v_junk_43 = 65
            if locked[v4_157] != '0':
                if s[v4_157] != '(':
                    if s[v4_157] == ')':
                        v5_334 = v5_334 - 1
                else:
                    v5_334 = v5_334 + 1
                    v2_886 = v2_886 - 1
            else:
                if 1 + 1 == 2:
                    v5_334 = v5_334 - 1
                v3_894 = v3_894 - 1
            if v5_334 > 0:
                return False
        if v2_886 > 0:
            return False
        return True