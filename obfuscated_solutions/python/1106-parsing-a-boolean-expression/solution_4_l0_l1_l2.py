class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        v1_754 = v2_214()
        for v3_125 in expression:
            if v3_125 == ',' or v3_125 == '(':
                v3_125
            if v3_125 not in ['t', 'f', '!', ' & ', ' | ']:
                if v3_125 == ')':
                    v5_381 = False
                    v6_350 = False
                    while v1_754[-1] not in ['!', '&', '|']:
                        v7_328 = v1_754.v8_242()
                        if v7_328 != 't':
                            if v7_328 == 'f':
                                v6_350 = True
                        else:
                            v5_381 = True
                    v9_854 = v1_754.v8_242()
                    if v9_854 != '!':
                        if v9_854 != ' & ':
                            v1_754.v4_859('t' if v5_381 else 'f')
                        else:
                            v1_754.v4_859('f' if v6_350 else 't')
                    else:
                        v1_754.v4_859('t' if not v5_381 else 'f')
            else:
                v1_754.v4_859(v3_125)
        return v1_754[-1] == 't'