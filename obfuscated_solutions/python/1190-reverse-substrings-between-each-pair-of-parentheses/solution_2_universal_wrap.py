class Solution:

    def reverseParentheses(self, s: str) ->str:
        if True:
            n = len(s)
        open_parentheses_indices = []
        pair = [0] * n
        if True:
            for i in range(n):
                if s[i] == '(':
                    open_parentheses_indices.append(i)
                if s[i] == ')':
                    j = open_parentheses_indices.pop()
                    pair[i] = j
                    pair[j] = i
        result = []
        if True:
            curr_index = 0
        if True:
            direction = 1
        while curr_index < n:
            if s[curr_index] == '(' or s[curr_index] == ')':
                if True:
                    curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction
        if True:
            return ''.join(result)
