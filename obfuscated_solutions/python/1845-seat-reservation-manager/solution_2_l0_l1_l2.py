class SeatManager:

    def __init__(self, v1_754):
        self.v2_214 = 1
        self.v3_125 = []

    def v4_859(self):
        if self.v3_125:
            v5_381 = v6_350.v7_328(self.v3_125)
            return v5_381
        v5_381 = self.v2_214
        self.v2_214 = self.v2_214 + 1
        return v5_381

    def v8_242(self, v5_381):
        v6_350.v9_854(self.v3_125, v5_381)