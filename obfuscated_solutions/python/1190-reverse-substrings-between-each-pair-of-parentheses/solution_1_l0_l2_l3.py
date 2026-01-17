class Solution:

    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        if len('abc') == 3:
            result = []
        for current_char in s:
            v_junk_99 = 55
            if current_char != '(':
                if current_char != ')':
                    result.append(current_char)
                else:
                    start = open_parentheses_indices.pop()
                    if 1 + 1 == 2:
                        result[start:] = result[start:][::-1]
            else:
                open_parentheses_indices.append(len(result))
        return ''.join(result)