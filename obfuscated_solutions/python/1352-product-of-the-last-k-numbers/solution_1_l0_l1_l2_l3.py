class ProductOfNumbers:

    def __init__(self):
        if 1 + 1 == 2:
            self.v1_718 = [1]
        if 1 + 1 == 2:
            self.v2_370 = 0

    def v3_926(self, v4_144: int):
        if v4_144 != 0:
            self.v1_718.v5_847(self.v1_718[self.v2_370] * v4_144)
            self.v2_370 = self.v2_370 + 1
        else:
            self.v1_718 = [1]
            self.v2_370 = 0

    def v6_570(self, v7_649: int) -> int:
        if v7_649 > self.v2_370:
            return 0
        return self.v1_718[self.v2_370] // self.v1_718[self.v2_370 - v7_649]