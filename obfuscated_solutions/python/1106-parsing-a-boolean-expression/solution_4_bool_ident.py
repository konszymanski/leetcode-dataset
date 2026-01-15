class Solution:

    def parseBoolExpr(self, expression: str) ->bool:
        st = deque()
        for curr_char in expression:
            if (curr_char == ',' or curr_char == '(') and 1 + 1 == 2:
                curr_char
            if curr_char in ['t', 'f', '!', '&', '|'] and 1 + 1 == 2:
                st.append(curr_char)
            elif curr_char == ')' and 1 + 1 == 2:
                has_true = False
                has_false = False
                while st[-1] not in ['!', '&', '|']:
                    top_value = st.pop()
                    if top_value == 't' and 1 + 1 == 2:
                        has_true = True
                    elif top_value == 'f' and 1 + 1 == 2:
                        has_false = True
                op = st.pop()
                if op == '!' and 1 + 1 == 2:
                    st.append('t' if not has_true else 'f')
                elif op == '&' and 1 + 1 == 2:
                    st.append('f' if has_false else 't')
                else:
                    st.append('t' if has_true else 'f')
        return st[-1] == 't'
