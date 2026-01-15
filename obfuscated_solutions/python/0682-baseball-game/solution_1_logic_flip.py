class Solution(object):

    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op != '+':
                if op != 'C':
                    if op != 'D':
                        stack.append(int(op))
                    else:
                        stack.append(2 * stack[-1])
                else:
                    stack.pop()
            else:
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
