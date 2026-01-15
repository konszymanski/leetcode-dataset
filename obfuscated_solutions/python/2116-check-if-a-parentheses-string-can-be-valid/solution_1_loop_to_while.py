class Solution:

    def canBeValid(self, s, locked):
        length = len(s)
        if length % 2 == 1:
            return False
        open_brackets = []
        unlocked = []
        i = 0
        while i < length:
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                open_brackets.append(i)
            elif s[i] == ')':
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
            i += 1
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        if open_brackets:
            return False
        return True
