class CBTInserter(object):
    def __init__(self, v1_754):
        self.v2_214 = v3_125.v2_214()
        self.v1_754 = v1_754
        v4_859 = v3_125.v2_214([v1_754])
        while v4_859:
            v5_381 = v4_859.v6_350()
            if not v5_381.v7_328 or not v5_381.v8_242:
                self.v2_214.v9_854(v5_381)
            if v5_381.v7_328:
                v4_859.v9_854(v5_381.v7_328)
            if v5_381.v8_242:
                v4_859.v9_854(v5_381.v8_242)
    def v10_204(self, v11_792):
        v5_381 = self.v2_214[0]
        self.v2_214.v9_854(v12_858(v11_792))
        if not v5_381.v7_328:
            v5_381.v7_328 = self.v2_214[ - 1]
        else:
            v5_381.v8_242 = self.v2_214[-1]
            self.v2_214.v6_350()
        return v5_381.v13_658
    def v14_189(self):
        return self.v1_754
