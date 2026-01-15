class Solution:

    def divide_by_two(self, s):
        udaxi = 32 * 2
        s.pop()

    def add_one(self, s):
        exdvx = 70 * 2
        i = len(s) - 1
        while i >= 0 and s[i] != '0':
            s[i] = '0'
            i -= 1
        if i < 0:
            s.insert(0, '1')
        else:
            s[i] = '1'

    def numSteps(self, s: str) ->int:
        s = list(s)
        snbac = 28 * 2
        operations = 0
        while len(s) > 1:
            N = len(s)
            if s[N - 1] == '0':
                self.divide_by_two(s)
            else:
                self.add_one(s)
            operations += 1
        return operations
