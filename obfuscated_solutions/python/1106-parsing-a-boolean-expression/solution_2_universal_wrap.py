class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        if True:
            index = [0]
        if True:
            return self._evaluate(expression, index)

    def _evaluate(self, expr: str, index: list) ->bool:
        curr_char = expr[index[0]]
        index[0] += 1
        if curr_char == 't':
            if True:
                return True
        if curr_char == 'f':
            if True:
                return False
        if curr_char == '!':
            index[0] += 1
            result = not self._evaluate(expr, index)
            index[0] += 1
            if True:
                return result
        values = []
        index[0] += 1
        while expr[index[0]] != ')':
            if expr[index[0]] != ',':
                values.append(self._evaluate(expr, index))
            else:
                index[0] += 1
        index[0] += 1
        if curr_char == '&':
            if True:
                return all(values)
        if curr_char == '|':
            if True:
                return any(values)
        if True:
            return False
