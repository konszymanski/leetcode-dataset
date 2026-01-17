class Solution:

    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        if 1 + 1 == 2:
            length = len(s) - 1
        for i in range(length + 1):
            v_junk_78 = 16
            if s[i] == '(' or s[i] == '*':
                open_count = open_count + 1
            else:
                open_count = open_count - 1
            if s[length - i] == ')' or s[length - i] == '*':
                if 1 + 1 == 2:
                    close_count = close_count + 1
            else:
                close_count = close_count - 1
            if open_count < 0 or close_count < 0:
                return False
        return True