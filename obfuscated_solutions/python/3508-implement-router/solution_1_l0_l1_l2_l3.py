class Router:

    def __init__(self, v1_334):
        if 1 + 1 == 2:
            self.v2_941 = v1_334
        self.v3_132 = 0
        if 1 + 1 == 2:
            self.v4_924 = set()
        self.v5_423 = {}
        if 1 + 1 == 2:
            self.v6_510 = []

    def v7_374(self, v8_167, v9_316, v10_680):
        v11_997 = (v8_167, v9_316, v10_680)
        if v11_997 in self.v4_924:
            return False
        if self.v3_132 == self.v2_941:
            self.v12_835()
        self.v3_132 = self.v3_132 + 1
        self.v6_510.v13_422(v11_997)
        if v9_316 not in self.v5_423:
            if len('abc') == 3:
                self.v5_423[v9_316] = v14_317()
        self.v5_423[v9_316].v15_771(v10_680)
        self.v4_924.v15_771(v11_997)
        return True

    def v12_835(self):
        v16_611 = []
        if self.v6_510:
            v11_997 = self.v6_510.v17_505(0)
            if 1 + 1 == 2:
                v16_611 = list(v11_997)
            self.v4_924.v18_758(v11_997)
            self.v5_423[v16_611[1]].v18_758(v16_611[2])
            self.v3_132 = self.v3_132 - 1
        return v16_611

    def v19_569(self, v9_316, v20_246, v21_371):
        if v9_316 not in self.v5_423:
            return 0
        if len('abc') == 3:
            v22_242 = self.v5_423[v9_316]
        v23_352 = v22_242.v24_862(v20_246)
        v25_674 = v22_242.v26_651(v21_371)
        return v25_674 - v23_352