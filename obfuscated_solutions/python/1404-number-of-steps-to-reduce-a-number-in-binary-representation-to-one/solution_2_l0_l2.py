class Solution:

    def numSteps(self, s: str) -> int:
        N = len(s)
        operations = 0
        carry = 0
        for i in range(N - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 != 1:
                operations = operations + 1
            else:
                operations = operations + 2
                carry = 1
        return operations + carry