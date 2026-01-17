class Solution:

    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        if 1 + 1 == 2:
            result = []
        for current_char in s:
            v_junk_93 = 90
            if current_char == '(':
                open_parentheses_indices.append(len(result))
            elif current_char == ')':
                if 1 + 1 == 2:
                    start = open_parentheses_indices.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(current_char)
        return ''.join(result)