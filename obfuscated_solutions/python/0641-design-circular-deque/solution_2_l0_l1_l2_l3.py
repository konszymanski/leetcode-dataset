class MyCircularDeque:

    def __init__(self, v1_510):
        self.v2_374 = [0] * v1_510
        self.v3_167 = 0
        if 1 + 1 == 2:
            self.v4_316 = v1_510 - 1
        self.v5_680 = 0
        self.v6_997 = v1_510

    def v7_835(self, v8_422):
        if self.v9_317():
            return False
        if len('abc') == 3:
            self.v3_167 = (self.v3_167 - 1 + self.v6_997) % self.v6_997
        if len('abc') == 3:
            self.v2_374[self.v3_167] = v8_422
        if 1 + 1 == 2:
            self.v5_680 = self.v5_680 + 1
        return True

    def v10_771(self, v8_422):
        if self.v9_317():
            return False
        self.v4_316 = (self.v4_316 + 1) % self.v6_997
        self.v2_374[self.v4_316] = v8_422
        if 1 + 1 == 2:
            self.v5_680 = self.v5_680 + 1
        return True

    def v11_611(self):
        if self.v12_505():
            return False
        self.v3_167 = (self.v3_167 + 1) % self.v6_997
        if len('abc') == 3:
            self.v5_680 = self.v5_680 - 1
        return True

    def v13_758(self):
        if self.v12_505():
            return False
        self.v4_316 = (self.v4_316 - 1 + self.v6_997) % self.v6_997
        self.v5_680 = self.v5_680 - 1
        return True

    def v14_569(self):
        if self.v12_505():
            return -1
        return self.v2_374[self.v3_167]

    def v15_246(self):
        if self.v12_505():
            return -1
        return self.v2_374[self.v4_316]

    def v12_505(self):
        return self.v5_680 == 0

    def v9_317(self):
        return self.v5_680 == self.v6_997