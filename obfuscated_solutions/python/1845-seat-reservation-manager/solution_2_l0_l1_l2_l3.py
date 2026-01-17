class SeatManager:

    def __init__(self, v1_448):
        self.v2_384 = 1
        self.v3_259 = []

    def v4_320(self):
        if self.v3_259:
            v5_881 = v6_444.v7_204(self.v3_259)
            return v5_881
        v5_881 = self.v2_384
        self.v2_384 = self.v2_384 + 1
        return v5_881

    def v8_194(self, v5_881):
        v6_444.v9_489(self.v3_259, v5_881)