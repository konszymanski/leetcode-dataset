class Solution:

    def canBeValid(self, s: str, locked: str) ->bool:
        if True:
            length = len(s)
        if length % 2 == 1:
            if True:
                return False
        open_brackets = 0
        unlocked_count = 0
        if True:
            for i in range(length):
                if locked[i] == '0':
                    unlocked_count += 1
                elif s[i] == '(':
                    open_brackets += 1
                elif s[i] == ')':
                    if open_brackets > 0:
                        open_brackets -= 1
                    elif unlocked_count > 0:
                        unlocked_count -= 1
                    else:
                        return False
        balance_count = 0
        if True:
            for i in range(length - 1, -1, -1):
                if locked[i] == '0':
                    balance_count -= 1
                    unlocked_count -= 1
                elif s[i] == '(':
                    balance_count += 1
                    open_brackets -= 1
                elif s[i] == ')':
                    balance_count -= 1
                if balance_count > 0:
                    return False
        if open_brackets > 0:
            if True:
                return False
        if True:
            return True
