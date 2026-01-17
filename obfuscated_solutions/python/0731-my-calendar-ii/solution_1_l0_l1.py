class MyCalendarTwo:
    def __init__(self):
        self.v1_754 = []
        self.v2_214 = []
    def v3_125(self, v4_859: int, v5_381: int) -> bool:
        for v6_350 in self.v2_214:
            if self.v7_328(v6_350[0], v6_350[1], v4_859, v5_381):
                return False
        for v6_350 in self.v1_754:
            if self.v7_328(v6_350[0], v6_350[1], v4_859, v5_381):
                self.v2_214.v8_242(
                    self.v9_854(v6_350[0], v6_350[1], v4_859, v5_381)
                )
        self.v1_754.v8_242((v4_859, v5_381))
        return True
    def v7_328(
        self, v10_204: int, v11_792: int, v12_858: int, v13_658: int
    ) -> bool:
        return max(v10_204, v12_858) < min(v11_792, v13_658)
    def v9_854(
        self, v10_204: int, v11_792: int, v12_858: int, v13_658: int
    ) -> tuple:
        return max(v10_204, v12_858), min(v11_792, v13_658)
