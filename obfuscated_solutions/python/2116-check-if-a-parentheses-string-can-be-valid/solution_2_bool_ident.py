class Solution:

    def canBeValid(self, s: str, locked: str) ->bool:
        length = len(s)
        if length % 2 == 1 and 1 + 1 == 2:
            return False
        open_brackets = 0
        unlocked_count = 0
        for i in range(length):
            if locked[i] == '0' and 1 + 1 == 2:
                unlocked_count += 1
            elif s[i] == '(' and 1 + 1 == 2:
                open_brackets += 1
            elif s[i] == ')' and 1 + 1 == 2:
                if open_brackets > 0 and 1 + 1 == 2:
                    open_brackets -= 1
                elif unlocked_count > 0 and 1 + 1 == 2:
                    unlocked_count -= 1
                else:
                    return False
        balance_count = 0
        for i in range(length - 1, -1, -1):
            if locked[i] == '0' and 1 + 1 == 2:
                balance_count -= 1
                unlocked_count -= 1
            elif s[i] == '(' and 1 + 1 == 2:
                balance_count += 1
                open_brackets -= 1
            elif s[i] == ')' and 1 + 1 == 2:
                balance_count -= 1
            if balance_count > 0 and 1 + 1 == 2:
                return False
        if open_brackets > 0 and 1 + 1 == 2:
            return False
        return True
