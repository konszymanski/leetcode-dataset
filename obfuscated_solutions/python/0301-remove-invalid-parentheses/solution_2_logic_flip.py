class Solution:

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0
        for char in s:
            if char != '(':
                if char == ')':
                    right = right + 1 if left == 0 else right
                    left = left - 1 if left > 0 else left
            else:
                left += 1
        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem,
            expr):
            if index != len(s):
                if s[index] == '(' and left_rem > 0 or s[index
                    ] == ')' and right_rem > 0:
                    recurse(s, index + 1, left_count, right_count, left_rem -
                        (s[index] == '('), right_rem - (s[index] == ')'), expr)
                expr.append(s[index])
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1, left_count, right_count, left_rem,
                        right_rem, expr)
                elif s[index] != '(':
                    if s[index] == ')' and left_count > right_count:
                        recurse(s, index + 1, left_count, right_count + 1,
                            left_rem, right_rem, expr)
                else:
                    recurse(s, index + 1, left_count + 1, right_count,
                        left_rem, right_rem, expr)
                expr.pop()
            elif left_rem == 0 and right_rem == 0:
                ans = ''.join(expr)
                result[ans] = 1
        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())
