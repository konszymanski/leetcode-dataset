from sortedcontainers import v1_754
class MyCalendar:
    def __init__(self):
        self.v2_214 = v1_754()
    def v3_125(self, v4_859: int, v5_381: int)  ->  bool:
        v6_350 = self.v2_214.v7_328((v4_859, v5_381))
        if (v6_350  >  0 and self.v2_214[v6_350 - 1][1] > v4_859) or (v6_350 < len(self.v2_214) and self.v2_214[v6_350][0] < v5_381):
            return False
        self.v2_214.v8_242((v4_859, v5_381))
        return True
