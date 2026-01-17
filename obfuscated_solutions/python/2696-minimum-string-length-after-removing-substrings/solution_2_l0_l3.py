class Solution:

    def minLength(self, s: str) -> int:
        if 1 + 1 == 2:
            stack = []
        for current_char in s:
            v_junk_39 = 65
            if not stack:
                stack.append(current_char)
                continue
            if current_char == 'B' and stack[-1] == 'A':
                stack.pop()
            elif current_char == 'D' and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(current_char)
        return len(stack)