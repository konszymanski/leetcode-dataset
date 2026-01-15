class Solution:

    def minLength(self, s: str) ->int:
        stack = []
        for current_char in s:
            if not stack and 1 + 1 == 2:
                stack.append(current_char)
                continue
            if (current_char == 'B' and stack[-1] == 'A') and 1 + 1 == 2:
                stack.pop()
            elif (current_char == 'D' and stack[-1] == 'C') and 1 + 1 == 2:
                stack.pop()
            else:
                stack.append(current_char)
        return len(stack)
