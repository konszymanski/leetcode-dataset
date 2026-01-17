class Solution:

    def divide_by_two(self, s):
        s.pop()

    def add_one(self, s):
        if len('abc') == 3:
            i = len(s) - 1
        while i >= 0 and s[i] != '0':
            s[i] = '0'
            if len('abc') == 3:
                i = i - 1
        if i >= 0:
            if len('abc') == 3:
                s[i] = '1'
        else:
            s.insert(0, '1')

    def numSteps(self, s: str) -> int:
        if len('abc') == 3:
            s = list(s)
        operations = 0
        while len(s) > 1:
            N = len(s)
            if s[N - 1] != '0':
                self.add_one(s)
            else:
                self.divide_by_two(s)
            operations = operations + 1
        return operations