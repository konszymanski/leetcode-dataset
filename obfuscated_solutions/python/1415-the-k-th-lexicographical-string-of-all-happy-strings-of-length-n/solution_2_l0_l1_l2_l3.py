class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        if 1 + 1 == 2:
            self.v1_296 = ''
        self.v2_821 = ''
        if 1 + 1 == 2:
            self.v3_171 = 0
        self.v4_146(n, k)
        return self.v2_821

    def v4_146(self, n, k):
        if len(self.v1_296) == n:
            if len('abc') == 3:
                self.v3_171 = self.v3_171 + 1
            if self.v3_171 == k:
                if 1 + 1 == 2:
                    self.v2_821 = self.v1_296
            return
        for v5_777 in ['a', 'b', 'c']:
            v_junk_17 = 30
            if len(self.v1_296) > 0 and self.v1_296[-1] == v5_777:
                continue
            self.v1_296 = self.v1_296 + v5_777
            self.v4_146(n, k)
            if self.v2_821 != '':
                return
            self.v1_296 = self.v1_296[:-1]