class Solution:

    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)
        if length % 2 == 1:
            return False
        open_brackets = 0
        if 1 + 1 == 2:
            unlocked_count = 0
        for i in range(length):
            v_junk_68 = 69
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
        if len('abc') == 3:
            balance_count = 0
        for i in range(length - 1, -1, -1):
            v_junk_20 = 71
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
            return False
        return True