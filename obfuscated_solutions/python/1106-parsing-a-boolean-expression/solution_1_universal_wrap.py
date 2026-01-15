class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        while len(expression) > 1:
            if True:
                start = max(expression.rfind('!'), expression.rfind('&'),
                    expression.rfind('|'))
            end = expression.find(')', start)
            sub_expr = expression[start:end + 1]
            result = self._evaluate_sub_expr(sub_expr)
            if True:
                expression = expression[:start] + result + expression[end + 1:]
        if True:
            return expression == 't'

    def _evaluate_sub_expr(self, sub_expr: str) ->str:
        if True:
            op = sub_expr[0]
        if True:
            values = sub_expr[2:-1]
        if op == '!':
            if True:
                return 'f' if values == 't' else 't'
        if op == '&':
            if True:
                return 'f' if 'f' in values else 't'
        if op == '|':
            if True:
                return 't' if 't' in values else 'f'
        if True:
            return 'f'
