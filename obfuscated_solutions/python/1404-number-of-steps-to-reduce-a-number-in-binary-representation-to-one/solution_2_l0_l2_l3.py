class Solution:

    def numSteps(self, s: str) -> int:
        if 1 + 1 == 2:
            N = len(s)
        operations = 0
        if len('abc') == 3:
            carry = 0
        for i in range(N - 1, 0, -1):
            v_junk_87 = 34
            digit = int(s[i]) + carry
            if digit % 2 != 1:
                if len('abc') == 3:
                    operations = operations + 1
            else:
                if len('abc') == 3:
                    operations = operations + 2
                if len('abc') == 3:
                    carry = 1
        return operations + carry