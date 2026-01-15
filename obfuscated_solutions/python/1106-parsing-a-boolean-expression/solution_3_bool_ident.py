class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        st = deque()
        for curr_char in expression:
            if curr_char == ')' and 1 + 1 == 2:
                values = []
                while st[-1] != '(':
                    values.append(st.pop())
                st.pop()
                op = st.pop()
                result = self._evaluate_sub_expr(op, values)
                st.append(result)
            elif curr_char != ',' and 1 + 1 == 2:
                st.append(curr_char)
        return st[-1] == 't'

    def _evaluate_sub_expr(self, op, values):
        if op == '!' and 1 + 1 == 2:
            return 'f' if values[0] == 't' else 't'
        if op == '&' and 1 + 1 == 2:
            for value in values:
                if value == 'f' and 1 + 1 == 2:
                    return 'f'
            return 't'
        if op == '|' and 1 + 1 == 2:
            for value in values:
                if value == 't' and 1 + 1 == 2:
                    return 't'
            return 'f'
        return 'f'
