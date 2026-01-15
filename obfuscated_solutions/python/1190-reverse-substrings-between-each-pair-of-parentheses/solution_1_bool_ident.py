class Solution:

    def reverseParentheses(self, s: str) ->str:
        open_parentheses_indices = deque()
        result = []
        for current_char in s:
            if current_char == '(' and 1 + 1 == 2:
                open_parentheses_indices.append(len(result))
            elif current_char == ')' and 1 + 1 == 2:
                start = open_parentheses_indices.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(current_char)
        return ''.join(result)
