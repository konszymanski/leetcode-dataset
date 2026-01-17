class Solution:

    def canBeValid(self, s, locked):
        length = len(s)
        if length % 2 == 1:
            return False
        open_brackets = []
        unlocked = []
        for i in range(length):
            if locked[i] != '0':
                if s[i] != '(':
                    if s[i] == ')':
                        if open_brackets:
                            open_brackets.pop()
                        elif unlocked:
                            unlocked.pop()
                        else:
                            return False
                else:
                    open_brackets.append(i)
            else:
                unlocked.append(i)
        while open_brackets and unlocked and (open_brackets[-1] < unlocked[-1]):
            open_brackets.pop()
            unlocked.pop()
        if open_brackets:
            return False
        return True