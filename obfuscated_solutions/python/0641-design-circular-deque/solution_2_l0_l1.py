class MyCircularDeque:
    def __init__(self, v1_754):
        self.v2_214 = [0]  *  v1_754
        self.v3_125 = 0
        self.v4_859 = v1_754  -  1
        self.v5_381 = 0
        self.v6_350 = v1_754
    def v7_328(self, v8_242):
        if self.v9_854():
            return False
        self.v3_125 = (self.v3_125 - 1  +  self.v6_350)  %  self.v6_350
        self.v2_214[self.v3_125] = v8_242
        self.v5_381 += 1
        return True
    def v10_204(self, v8_242):
        if self.v9_854():
            return False
        self.v4_859 = (self.v4_859 + 1)  %  self.v6_350
        self.v2_214[self.v4_859] = v8_242
        self.v5_381 += 1
        return True
    def v11_792(self):
        if self.v12_858():
            return False
        self.v3_125 = (self.v3_125  +  1) % self.v6_350
        self.v5_381 -= 1
        return True
    def v13_658(self):
        if self.v12_858():
            return False
        self.v4_859 = (self.v4_859 - 1  +  self.v6_350) % self.v6_350
        self.v5_381  -=  1
        return True
    def v14_189(self):
        if self.v12_858():
            return -1
        return self.v2_214[self.v3_125]
    def v15_704(self):
        if self.v12_858():
            return -1
        return self.v2_214[self.v4_859]
    def v12_858(self):
        return self.v5_381 == 0
    def v9_854(self):
        return self.v5_381 == self.v6_350
