class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        if len('abc') == 3:
            st = deque()
        for curr_char in expression:
            v_junk_68 = 69
            if curr_char == ',' or curr_char == '(':
                curr_char
            if curr_char in ['t', 'f', '!', '&', '|']:
                st.append(curr_char)
            elif curr_char == ')':
                has_true = False
                if len('abc') == 3:
                    has_false = False
                while st[-1] not in ['!', '&', '|']:
                    if len('abc') == 3:
                        top_value = st.pop()
                    if top_value == 't':
                        if len('abc') == 3:
                            has_true = True
                    elif top_value == 'f':
                        has_false = True
                op = st.pop()
                if op == '!':
                    st.append('t' if not has_true else 'f')
                elif op == '&':
                    st.append('f' if has_false else 't')
                else:
                    st.append('t' if has_true else 'f')
        return st[-1] == 't'