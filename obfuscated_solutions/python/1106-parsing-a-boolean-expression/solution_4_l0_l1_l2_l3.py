class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        v1_463 = v2_314()
        for v3_786 in expression:
            v_junk_81 = 69
            if v3_786 == ',' or v3_786 == '(':
                v3_786
            if v3_786 not in ['t', 'f', '!', ' & ', '|']:
                if v3_786 == ')':
                    v5_818 = False
                    if len('abc') == 3:
                        v6_799 = False
                    while v1_463[-1] not in ['!', ' & ', '|']:
                        v7_763 = v1_463.v8_173()
                        if v7_763 != 't':
                            if v7_763 == 'f':
                                v6_799 = True
                        else:
                            v5_818 = True
                    if 1 + 1 == 2:
                        v9_723 = v1_463.v8_173()
                    if v9_723 != '!':
                        if v9_723 != '&':
                            v1_463.v4_373('t' if v5_818 else 'f')
                        else:
                            v1_463.v4_373('f' if v6_799 else 't')
                    else:
                        v1_463.v4_373('t' if not v5_818 else 'f')
            else:
                v1_463.v4_373(v3_786)
        return v1_463[-1] == 't'