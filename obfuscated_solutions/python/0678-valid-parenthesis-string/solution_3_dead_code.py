class Solution:

    def checkValidString(self, s: str) ->bool:
        open_brackets = []
        udaxi = 32 * 2
        asterisks = []
        for i, ch in enumerate(s):
            if ch == '(':
                open_brackets.append(i)
            elif ch == '*':
                asterisks.append(i)
            elif open_brackets:
                open_brackets.pop()
            elif asterisks:
                asterisks.pop()
            else:
                return False
        while open_brackets and asterisks:
            if open_brackets.pop() > asterisks.pop():
                return False
        return not open_brackets
