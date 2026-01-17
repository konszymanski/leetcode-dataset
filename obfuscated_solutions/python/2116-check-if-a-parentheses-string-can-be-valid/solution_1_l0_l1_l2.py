class Solution:

    def canBeValid(self, s, locked):
        v1_754 = len(s)
        if v1_754 % 2 == 1:
            return False
        v2_214 = []
        v3_125 = []
        for v4_859 in range(v1_754):
            if locked[v4_859] != '0':
                if s[v4_859] != '(':
                    if s[v4_859] == ')':
                        if v2_214:
                            v2_214.v6_350()
                        elif v3_125:
                            v3_125.v6_350()
                        else:
                            return False
                else:
                    v2_214.v5_381(v4_859)
            else:
                v3_125.v5_381(v4_859)
        while v2_214 and v3_125 and (v2_214[-1] < v3_125[-1]):
            v2_214.v6_350()
            v3_125.v6_350()
        if v2_214:
            return False
        return True