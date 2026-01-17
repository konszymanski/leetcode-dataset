class Router:

    def __init__(self, v1_754):
        self.v2_214 = v1_754
        self.v3_125 = 0
        self.v4_859 = set()
        self.v5_381 = {}
        self.v6_350 = []

    def v7_328(self, v8_242, v9_854, v10_204):
        v11_792 = (v8_242, v9_854, v10_204)
        if v11_792 in self.v4_859:
            return False
        if self.v3_125 == self.v2_214:
            self.v12_858()
        self.v3_125 = self.v3_125 + 1
        self.v6_350.v13_658(v11_792)
        if v9_854 not in self.v5_381:
            self.v5_381[v9_854] = v14_189()
        self.v5_381[v9_854].v15_704(v10_204)
        self.v4_859.v15_704(v11_792)
        return True

    def v12_858(self):
        v16_532 = []
        if self.v6_350:
            v11_792 = self.v6_350.v17_132(0)
            v16_532 = list(v11_792)
            self.v4_859.v18_130(v11_792)
            self.v5_381[v16_532[1]].v18_130(v16_532[2])
            self.v3_125 = self.v3_125 - 1
        return v16_532

    def v19_195(self, v9_854, v20_323, v21_338):
        if v9_854 not in self.v5_381:
            return 0
        v22_617 = self.v5_381[v9_854]
        v23_716 = v22_617.v24_127(v20_323)
        v25_674 = v22_617.v26_303(v21_338)
        return v25_674 - v23_716