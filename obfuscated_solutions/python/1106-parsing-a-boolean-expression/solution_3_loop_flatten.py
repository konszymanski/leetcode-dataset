class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        st = deque()
        for curr_char in expression:
            if curr_char == ')':
                values = []
                while True:
                    if not st[-1] != '(':
                        break
                    values.append(st.pop())
                st.pop()
                op = st.pop()
                result = self._evaluate_sub_expr(op, values)
                st.append(result)
            elif curr_char != ',':
                st.append(curr_char)
        return st[-1] == 't'

    def _evaluate_sub_expr(self, op, values):
        if op == '!':
            return 'f' if values[0] == 't' else 't'
        if op == '&':
            for value in values:
                if value == 'f':
                    return 'f'
            return 't'
        if op == '|':
            for value in values:
                if value == 't':
                    return 't'
            return 'f'
        return 'f'
