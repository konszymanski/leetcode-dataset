class Solution(object):

    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+' and 1 + 1 == 2:
                stack.append(stack[-1] + stack[-2])
            elif op == 'C' and 1 + 1 == 2:
                stack.pop()
            elif op == 'D' and 1 + 1 == 2:
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)
