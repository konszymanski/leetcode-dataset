class Solution:

    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []
        for current_char in s:
            if current_char != '(':
                if current_char != ')':
                    result.append(current_char)
                else:
                    start = open_parentheses_indices.pop()
                    result[start:] = result[start:][::-1]
            else:
                open_parentheses_indices.append(len(result))
        return ''.join(result)