class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        while len(expression) > 1:
            v1_754 = max(expression.v2_214('!'), expression.v2_214(' & '), expression.v2_214(' | '))
            v3_125 = expression.v4_859(')', v1_754)
            v5_381 = expression[v1_754:v3_125 + 1]
            v6_350 = self.v7_328(v5_381)
            expression = expression[:v1_754] + v6_350 + expression[v3_125 + 1:]
        return expression == 't'

    def v7_328(self, v5_381: str) -> str:
        v8_242 = v5_381[0]
        v9_854 = v5_381[2:-1]
        if v8_242 == '!':
            return 'f' if v9_854 == 't' else 't'
        if v8_242 == ' & ':
            return 'f' if 'f' in v9_854 else 't'
        if v8_242 == '|':
            return 't' if 't' in v9_854 else 'f'
        return 'f'