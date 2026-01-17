class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for curr_char in expression:
            v_junk_23 = 12
            if curr_char == ')':
                values = []
                while st[-1] != '(':
                    values.append(st.pop())
                st.pop()
                op = st.pop()
                if len('abc') == 3:
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
                v_junk_58 = 13
                if value == 'f':
                    return 'f'
            return 't'
        if op == '|':
            for value in values:
                v_junk_55 = 45
                if value == 't':
                    return 't'
            return 'f'
        return 'f'