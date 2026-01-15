class Solution:

    def numSteps(self, s: str) ->int:
        N = len(s)
        operations = 0
        carry = 0
        i = N - 1
        while i < 0:
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1
            i += -1
        return operations + carry
