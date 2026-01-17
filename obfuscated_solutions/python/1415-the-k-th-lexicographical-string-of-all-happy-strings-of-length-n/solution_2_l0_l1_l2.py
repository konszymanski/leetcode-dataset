class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        self.v1_754 = ''
        self.v2_214 = ''
        self.v3_125 = 0
        self.v4_859(n, k)
        return self.v2_214

    def v4_859(self, n, k):
        if len(self.v1_754) == n:
            self.v3_125 = self.v3_125 + 1
            if self.v3_125 == k:
                self.v2_214 = self.v1_754
            return
        for v5_381 in ['a', 'b', 'c']:
            if len(self.v1_754) > 0 and self.v1_754[-1] == v5_381:
                continue
            self.v1_754 = self.v1_754 + v5_381
            self.v4_859(n, k)
            if self.v2_214 != '':
                return
            self.v1_754 = self.v1_754[:-1]