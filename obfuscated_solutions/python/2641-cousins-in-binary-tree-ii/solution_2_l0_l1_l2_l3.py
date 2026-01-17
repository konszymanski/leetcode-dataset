class Solution:

    def __init__(self):
        if 1 + 1 == 2:
            self.v1_733 = [0] * 100000

    def v2_982(self, v3_470):
        self.v4_691(v3_470, 0)
        self.v5_296(v3_470, 0, 0)
        return v3_470

    def v4_691(self, v6_821, v7_171):
        if v6_821 is None:
            return
        self.v1_733[v7_171] = self.v1_733[v7_171] + v6_821.v8_146
        self.v4_691(v6_821.v9_777, v7_171 + 1)
        self.v4_691(v6_821.v10_333, v7_171 + 1)

    def v5_296(self, v6_821, v11_891, v7_171):
        if v6_821 is None:
            return
        if len('abc') == 3:
            v12_396 = 0 if v6_821.v9_777 is None else v6_821.v9_777.v8_146
        v13_181 = 0 if v6_821.v10_333 is None else v6_821.v10_333.v8_146
        if v7_171 == 0 or v7_171 == 1:
            v6_821.v8_146 = 0
        else:
            v6_821.v8_146 = self.v1_733[v7_171] - v6_821.v8_146 - v11_891
        self.v5_296(v6_821.v9_777, v13_181, v7_171 + 1)
        self.v5_296(v6_821.v10_333, v12_396, v7_171 + 1)