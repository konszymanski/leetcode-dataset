class Solution:
    v1_754 = 1000000007

    def power(self, base, exponent):
        v2_214 = 1
        while exponent > 0:
            if exponent & 1:
                v2_214 = v2_214 * base % self.v1_754
            exponent = exponent >> 1
            base = base * base % self.v1_754
        return v2_214

    def v3_125(self, v4_859):
        self.v5_381 = [1] * (v4_859 + 1)
        self.v6_350 = [1] * (v4_859 + 1)
        for v7_328 in range(1, v4_859 + 1):
            self.v5_381[v7_328] = self.v5_381[v7_328 - 1] * v7_328 % self.v1_754
            self.v6_350[v7_328] = self.power(self.v5_381[v7_328], self.v1_754 - 2)

    def v8_242(self, v4_859, v9_854, v10_204):
        self.v3_125(v4_859)
        v11_792 = 1
        v12_858 = 0
        for v7_328 in range(v4_859, v10_204 - 1, -1):
            v13_658 = self.power(v7_328 - v10_204, v9_854 - v10_204)
            v13_658 = v13_658 * self.v6_350[v4_859 - v7_328] % self.v1_754
            v13_658 = v13_658 * self.v6_350[v7_328 - v10_204] % self.v1_754
            v12_858 = (v12_858 + v11_792 * v13_658 + self.v1_754) % self.v1_754
            v11_792 = v11_792 * -1
        return self.v5_381[v4_859] * v12_858 % self.v1_754