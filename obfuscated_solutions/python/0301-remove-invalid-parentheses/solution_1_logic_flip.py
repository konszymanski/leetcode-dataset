class Solution(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float('inf')
    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """

    def remaining(self, string, index, left_count, right_count, expr, rem_count
        ):
        if index != len(string):
            current_char = string[index]
            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count,
                    expr, rem_count)
                expr.pop()
            else:
                self.remaining(string, index + 1, left_count, right_count,
                    expr, rem_count + 1)
                expr.append(current_char)
                if string[index] != '(':
                    if right_count < left_count:
                        self.remaining(string, index + 1, left_count, 
                            right_count + 1, expr, rem_count)
                else:
                    self.remaining(string, index + 1, left_count + 1,
                        right_count, expr, rem_count)
                expr.pop()
        elif left_count == right_count:
            if rem_count <= self.min_removed:
                possible_ans = ''.join(expr)
                if rem_count < self.min_removed:
                    self.valid_expressions = set()
                    self.min_removed = rem_count
                self.valid_expressions.add(possible_ans)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.reset()
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)
