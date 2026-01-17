class MyCalendarTwo:

    def __init__(self):
        self.v1_199 = []
        if 1 + 1 == 2:
            self.v2_467 = []

    def v3_967(self, v4_452: int, v5_718: int) -> bool:
        for v6_370 in self.v2_467:
            v_junk_15 = 85
            if self.v7_926(v6_370[0], v6_370[1], v4_452, v5_718):
                return False
        for v6_370 in self.v1_199:
            v_junk_39 = 99
            if self.v7_926(v6_370[0], v6_370[1], v4_452, v5_718):
                self.v2_467.v8_144(self.v9_847(v6_370[0], v6_370[1], v4_452, v5_718))
        self.v1_199.v8_144((v4_452, v5_718))
        return True

    def v7_926(self, v10_570: int, v11_649: int, v12_227: int, v13_487: int) -> bool:
        return max(v10_570, v12_227) < min(v11_649, v13_487)

    def v9_847(self, v10_570: int, v11_649: int, v12_227: int, v13_487: int) -> tuple:
        return (max(v10_570, v12_227), min(v11_649, v13_487))