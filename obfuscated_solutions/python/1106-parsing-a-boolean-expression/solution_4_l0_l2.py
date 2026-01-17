class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for curr_char in expression:
            if curr_char == ',' or curr_char == '(':
                curr_char
            if curr_char not in ['t', 'f', '!', '&', '|']:
                if curr_char == ')':
                    has_true = False
                    has_false = False
                    while st[-1] not in ['!', '&', '|']:
                        top_value = st.pop()
                        if top_value != 't':
                            if top_value == 'f':
                                has_false = True
                        else:
                            has_true = True
                    op = st.pop()
                    if op != '!':
                        if op != '&':
                            st.append('t' if has_true else 'f')
                        else:
                            st.append('f' if has_false else 't')
                    else:
                        st.append('t' if not has_true else 'f')
            else:
                st.append(curr_char)
        return st[-1] == 't'