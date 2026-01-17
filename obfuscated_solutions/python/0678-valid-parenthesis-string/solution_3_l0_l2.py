class Solution:

    def checkValidString(self, s: str) -> bool:
        open_brackets = []
        asterisks = []
        for (i, ch) in enumerate(s):
            if ch != '(':
                if ch != '*':
                    if open_brackets:
                        open_brackets.pop()
                    elif asterisks:
                        asterisks.pop()
                    else:
                        return False
                else:
                    asterisks.append(i)
            else:
                open_brackets.append(i)
        while open_brackets and asterisks:
            if open_brackets.pop() > asterisks.pop():
                return False
        return not open_brackets