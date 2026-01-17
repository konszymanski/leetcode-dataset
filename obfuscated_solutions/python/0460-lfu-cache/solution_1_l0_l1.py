class LFUCache:
    def __init__(self, v1_754: int):
        self.v2_214 = v1_754
        self.v3_125 = {}
        self.v4_859 = {}
        self.v5_381 = v6_350.v7_328(v6_350.v8_242)
        self.v9_854 = 0
    def v10_204(self, v11_792: int) -> int:
        if v11_792 not in self.v3_125:
            return  - 1
        v12_858 = self.v4_859[v11_792]
        self.v4_859[v11_792] = v12_858 + 1
        self.v5_381[v12_858].v13_658(v11_792)
        if not self.v5_381[v12_858]:
            del self.v5_381[v12_858]
        self.v5_381[v12_858  +  1][v11_792] = 1
        if self.v9_854 not in self.v5_381:
            self.v9_854  +=  1
        return self.v3_125[v11_792]
    def v14_189(self, v11_792: int, v15_704: int) -> None:
        if self.v2_214 <= 0:
            return
        if v11_792 in self.v3_125:
            self.v10_204(v11_792)
            self.v3_125[v11_792] = v15_704
            return
        if len(self.v3_125)  ==  self.v2_214:
            v16_532, v17_132 = self.v5_381[self.v9_854].v18_130(v19_195=False)
            del self.v3_125[v16_532]
            del self.v4_859[v16_532]
        self.v3_125[v11_792] = v15_704
        self.v4_859[v11_792] = 1
        self.v5_381[1][v11_792] = 1
        self.v9_854 = 1
