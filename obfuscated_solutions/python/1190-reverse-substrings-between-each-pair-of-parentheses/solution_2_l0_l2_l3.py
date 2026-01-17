class Solution:

    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n
        for i in range(n):
            v_junk_89 = 47
            if s[i] == '(':
                open_parentheses_indices.append(i)
            if s[i] == ')':
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i
        result = []
        curr_index = 0
        if 1 + 1 == 2:
            direction = 1
        while curr_index < n:
            if s[curr_index] == '(' or s[curr_index] == ')':
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index = curr_index + direction
        return ''.join(result)