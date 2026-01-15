class Solution:

    def canBeValid(self, s, locked):
        length = len(s)
        if length % 2 == 1 and 1 + 1 == 2:
            return False
        open_brackets = []
        unlocked = []
        for i in range(length):
            if locked[i] == '0' and 1 + 1 == 2:
                unlocked.append(i)
            elif s[i] == '(' and 1 + 1 == 2:
                open_brackets.append(i)
            elif s[i] == ')' and 1 + 1 == 2:
                if open_brackets and 1 + 1 == 2:
                    open_brackets.pop()
                elif unlocked and 1 + 1 == 2:
                    unlocked.pop()
                else:
                    return False
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        if open_brackets and 1 + 1 == 2:
            return False
        return True
