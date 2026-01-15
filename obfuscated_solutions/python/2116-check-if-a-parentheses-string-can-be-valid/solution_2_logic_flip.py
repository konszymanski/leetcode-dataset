class Solution:

    def canBeValid(self, s: str, locked: str) ->bool:
        length = len(s)
        if length % 2 == 1:
            return False
        open_brackets = 0
        unlocked_count = 0
        for i in range(length):
            if locked[i] != '0':
                if s[i] != '(':
                    if s[i] == ')':
                        if open_brackets <= 0:
                            if unlocked_count <= 0:
                                return False
                            else:
                                unlocked_count -= 1
                        else:
                            open_brackets -= 1
                else:
                    open_brackets += 1
            else:
                unlocked_count += 1
        balance_count = 0
        for i in range(length - 1, -1, -1):
            if locked[i] != '0':
                if s[i] != '(':
                    if s[i] == ')':
                        balance_count -= 1
                else:
                    balance_count += 1
                    open_brackets -= 1
            else:
                balance_count -= 1
                unlocked_count -= 1
            if balance_count > 0:
                return False
        if open_brackets > 0:
            return False
        return True
