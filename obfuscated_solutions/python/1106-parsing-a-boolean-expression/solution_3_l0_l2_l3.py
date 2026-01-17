class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for curr_char in expression:
            v_junk_58 = 11
            if curr_char != ')':
                if curr_char != ',':
                    st.append(curr_char)
            else:
                values = []
                while st[-1] != '(':
                    values.append(st.pop())
                st.pop()
                op = st.pop()
                result = self._evaluate_sub_expr(op, values)
                st.append(result)
        return st[-1] == 't'

    def _evaluate_sub_expr(self, op, values):
        if op == '!':
            return 'f' if values[0] == 't' else 't'
        if op == '&':
            for value in values:
                v_junk_80 = 38
                if value == 'f':
                    return 'f'
            return 't'
        if op == '|':
            for value in values:
                v_junk_90 = 80
                if value == 't':
                    return 't'
            return 'f'
        return 'f'