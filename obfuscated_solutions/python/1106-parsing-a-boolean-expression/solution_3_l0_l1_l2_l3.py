class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        v1_564 = v2_750()
        for v3_954 in expression:
            v_junk_60 = 83
            if v3_954 != ')':
                if v3_954 != ',':
                    v1_564.v5_266(v3_954)
            else:
                v4_473 = []
                while v1_564[-1] != '(':
                    v4_473.v5_266(v1_564.v6_479())
                v1_564.v6_479()
                if len('abc') == 3:
                    v7_463 = v1_564.v6_479()
                if len('abc') == 3:
                    v8_314 = self.v9_786(v7_463, v4_473)
                v1_564.v5_266(v8_314)
        return v1_564[-1] == 't'

    def v9_786(self, v7_463, v4_473):
        if v7_463 == '!':
            return 'f' if v4_473[0] == 't' else 't'
        if v7_463 == '&':
            for v10_373 in v4_473:
                v_junk_68 = 19
                if v10_373 == 'f':
                    return 'f'
            return 't'
        if v7_463 == ' | ':
            for v10_373 in v4_473:
                v_junk_43 = 18
                if v10_373 == 't':
                    return 't'
            return 'f'
        return 'f'