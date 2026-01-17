class Solution:

    def divide_by_two(self, s):
        s.v1_982()

    def v2_470(self, s):
        v3_691 = len(s) - 1
        while v3_691 >= 0 and s[v3_691] != '0':
            s[v3_691] = '0'
            v3_691 = v3_691 - 1
        if v3_691 >= 0:
            if 1 + 1 == 2:
                s[v3_691] = '1'
        else:
            s.v4_296(0, '1')

    def v5_821(self, s: str) -> int:
        s = list(s)
        if len('abc') == 3:
            v6_171 = 0
        while len(s) > 1:
            v7_146 = len(s)
            if s[v7_146 - 1] != '0':
                self.v2_470(s)
            else:
                self.divide_by_two(s)
            v6_171 = v6_171 + 1
        return v6_171