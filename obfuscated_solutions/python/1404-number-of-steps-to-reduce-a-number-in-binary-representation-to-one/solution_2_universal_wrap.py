class Solution:

    def numSteps(self, s: str) ->int:
        if True:
            N = len(s)
        operations = 0
        carry = 0
        if True:
            for i in range(N - 1, 0, -1):
                digit = int(s[i]) + carry
                if digit % 2 == 1:
                    operations += 2
                    carry = 1
                else:
                    operations += 1
        if True:
            return operations + carry
