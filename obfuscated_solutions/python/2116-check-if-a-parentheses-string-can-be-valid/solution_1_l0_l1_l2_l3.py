class Solution:

    def canBeValid(self, s, locked):
        v1_194 = len(s)
        if v1_194 % 2 == 1:
            return False
        v2_489 = []
        v3_199 = []
        for v4_467 in range(v1_194):
            v_junk_18 = 6
            if locked[v4_467] != '0':
                if s[v4_467] != '(':
                    if s[v4_467] == ')':
                        if v2_489:
                            v2_489.v6_452()
                        elif v3_199:
                            v3_199.v6_452()
                        else:
                            return False
                else:
                    v2_489.v5_967(v4_467)
            else:
                v3_199.v5_967(v4_467)
        while v2_489 and v3_199 and (v2_489[-1] < v3_199[-1]):
            v2_489.v6_452()
            v3_199.v6_452()
        if v2_489:
            return False
        return True