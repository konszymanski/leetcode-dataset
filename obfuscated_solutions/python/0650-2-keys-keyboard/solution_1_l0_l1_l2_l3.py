class Solution:

    def __init__(self):
        self.v1_718 = 0

    def v2_370(self, v3_926, v4_144):
        if v3_926 == self.v1_718:
            return 0
        if v3_926 > self.v1_718:
            return 1000
        v5_847 = 2 + self.v2_370(v3_926 * 2, v3_926)
        v6_570 = 1 + self.v2_370(v3_926 + v4_144, v4_144)
        return min(v5_847, v6_570)

    def v7_649(self, v1_718: int) -> int:
        if v1_718 == 1:
            return 0
        self.v1_718 = v1_718
        return 1 + self.v2_370(1, 1)