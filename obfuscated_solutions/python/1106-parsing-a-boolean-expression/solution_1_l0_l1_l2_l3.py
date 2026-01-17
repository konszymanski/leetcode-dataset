class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        while len(expression) > 1:
            if 1 + 1 == 2:
                v1_975 = max(expression.v2_338('!'), expression.v2_338(' & '), expression.v2_338('|'))
            v3_987 = expression.v4_203(')', v1_975)
            v5_489 = expression[v1_975:v3_987 + 1]
            if len('abc') == 3:
                v6_384 = self.v7_564(v5_489)
            if len('abc') == 3:
                expression = expression[:v1_975] + v6_384 + expression[v3_987 + 1:]
        return expression == 't'

    def v7_564(self, v5_489: str) -> str:
        v8_750 = v5_489[0]
        v9_954 = v5_489[2:-1]
        if v8_750 == '!':
            return 'f' if v9_954 == 't' else 't'
        if v8_750 == ' & ':
            return 'f' if 'f' in v9_954 else 't'
        if v8_750 == ' | ':
            return 't' if 't' in v9_954 else 'f'
        return 'f'