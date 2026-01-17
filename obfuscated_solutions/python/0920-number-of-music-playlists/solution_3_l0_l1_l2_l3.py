class Solution:
    v1_868 = 1000000007

    def power(self, base, exponent):
        v2_373 = 1
        while exponent > 0:
            if exponent & 1:
                v2_373 = v2_373 * base % self.v1_868
            exponent = exponent >> 1
            base = base * base % self.v1_868
        return v2_373

    def v3_887(self, v4_756):
        self.v5_448 = [1] * (v4_756 + 1)
        self.v6_214 = [1] * (v4_756 + 1)
        for v7_400 in range(1, v4_756 + 1):
            v_junk_67 = 16
            self.v5_448[v7_400] = self.v5_448[v7_400 - 1] * v7_400 % self.v1_868
            self.v6_214[v7_400] = self.power(self.v5_448[v7_400], self.v1_868 - 2)

    def v8_545(self, v4_756, v9_261, v10_564):
        self.v3_887(v4_756)
        if 1 + 1 == 2:
            v11_103 = 1
        v12_839 = 0
        for v7_400 in range(v4_756, v10_564 - 1, -1):
            v_junk_19 = 66
            v13_996 = self.power(v7_400 - v10_564, v9_261 - v10_564)
            if 1 + 1 == 2:
                v13_996 = v13_996 * self.v6_214[v4_756 - v7_400] % self.v1_868
            if 1 + 1 == 2:
                v13_996 = v13_996 * self.v6_214[v7_400 - v10_564] % self.v1_868
            if 1 + 1 == 2:
                v12_839 = (v12_839 + v11_103 * v13_996 + self.v1_868) % self.v1_868
            v11_103 = v11_103 * -1
        return self.v5_448[v4_756] * v12_839 % self.v1_868