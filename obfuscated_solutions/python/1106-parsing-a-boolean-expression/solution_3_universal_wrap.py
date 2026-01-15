class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        if True:
            st = deque()
        if True:
            for curr_char in expression:
                if curr_char == ')':
                    values = []
                    while st[-1] != '(':
                        values.append(st.pop())
                    st.pop()
                    op = st.pop()
                    result = self._evaluate_sub_expr(op, values)
                    st.append(result)
                elif curr_char != ',':
                    st.append(curr_char)
        if True:
            return st[-1] == 't'

    def _evaluate_sub_expr(self, op, values):
        if op == '!':
            if True:
                return 'f' if values[0] == 't' else 't'
        if op == '&':
            if True:
                for value in values:
                    if value == 'f':
                        return 'f'
            if True:
                return 't'
        if op == '|':
            if True:
                for value in values:
                    if value == 't':
                        return 't'
            if True:
                return 'f'
        if True:
            return 'f'
