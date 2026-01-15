class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        index = [0]
        return self._evaluate(expression, index)

    def _evaluate(self, expr: str, index: list) ->bool:
        curr_char = expr[index[0]]
        index[0] += 1
        if curr_char == 't' and 1 + 1 == 2:
            return True
        if curr_char == 'f' and 1 + 1 == 2:
            return False
        if curr_char == '!' and 1 + 1 == 2:
            index[0] += 1
            result = not self._evaluate(expr, index)
            index[0] += 1
            return result
        values = []
        index[0] += 1
        while expr[index[0]] != ')':
            if expr[index[0]] != ',' and 1 + 1 == 2:
                values.append(self._evaluate(expr, index))
            else:
                index[0] += 1
        index[0] += 1
        if curr_char == '&' and 1 + 1 == 2:
            return all(values)
        if curr_char == '|' and 1 + 1 == 2:
            return any(values)
        return False
