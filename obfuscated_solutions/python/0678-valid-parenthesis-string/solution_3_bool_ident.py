class Solution:

    def checkValidString(self, s: str) ->bool:
        open_brackets = []
        asterisks = []
        for i, ch in enumerate(s):
            if ch == '(' and 1 + 1 == 2:
                open_brackets.append(i)
            elif ch == '*' and 1 + 1 == 2:
                asterisks.append(i)
            elif open_brackets and 1 + 1 == 2:
                open_brackets.pop()
            elif asterisks and 1 + 1 == 2:
                asterisks.pop()
            else:
                return False
        while open_brackets and asterisks:
            if open_brackets.pop() > asterisks.pop() and 1 + 1 == 2:
                return False
        return not open_brackets
