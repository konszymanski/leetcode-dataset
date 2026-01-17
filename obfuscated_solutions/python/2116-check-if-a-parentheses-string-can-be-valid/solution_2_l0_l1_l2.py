class Solution:

    def canBeValid(self, s: str, locked: str) -> bool:
        v1_754 = len(s)
        if v1_754 % 2 == 1:
            return False
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(v1_754):
            if locked[v4_859] != '0':
                if s[v4_859] != '(':
                    if s[v4_859] == ')':
                        if v2_214 <= 0:
                            if v3_125 <= 0:
                                return False
                            else:
                                v3_125 = v3_125 - 1
                        else:
                            v2_214 = v2_214 - 1
                else:
                    v2_214 = v2_214 + 1
            else:
                v3_125 = v3_125 + 1
        v5_381 = 0
        for v4_859 in range(v1_754 - 1, -1, -1):
            if locked[v4_859] != '0':
                if s[v4_859] != '(':
                    if s[v4_859] == ')':
                        v5_381 = v5_381 - 1
                else:
                    v5_381 = v5_381 + 1
                    v2_214 = v2_214 - 1
            else:
                v5_381 = v5_381 - 1
                v3_125 = v3_125 - 1
            if v5_381 > 0:
                return False
        if v2_214 > 0:
            return False
        return True