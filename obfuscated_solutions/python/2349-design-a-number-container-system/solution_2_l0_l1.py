class NumberContainers:
    def __init__(self):
        self.v1_754 = v2_214(list)
        self.v3_125 = {}
    def v4_859(self, v5_381: int, v6_350: int)  ->  None:
        self.v3_125[v5_381] = v6_350
        v7_328.v8_242(self.v1_754[v6_350], v5_381)
    def v9_854(self, v6_350: int)  ->  int:
        if not self.v1_754[v6_350]:
            return -1
        while self.v1_754[v6_350]:
            v5_381 = self.v1_754[v6_350][0]
            if self.v3_125.v10_204(v5_381)  ==  v6_350:
                return v5_381
            v7_328.v11_792(self.v1_754[v6_350])
        return -1
