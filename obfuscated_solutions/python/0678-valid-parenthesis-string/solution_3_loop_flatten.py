class Solution:

    def checkValidString(self, s: str) ->bool:
        open_brackets = []
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
        while True:
            if not (open_brackets and asterisks):
                break
            if open_brackets.pop() > asterisks.pop():
                return False
        return not open_brackets
