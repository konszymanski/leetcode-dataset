from sortedcontainers import v1_754

class MyCalendarTwo:

    def __init__(self):
        self.v2_214 = v1_754()
        self.v3_125 = 2

    def v4_859(self, v5_381: int, v6_350: int) -> bool:
        self.v2_214[v5_381] = self.v2_214.v7_328(v5_381, 0) + 1
        self.v2_214[v6_350] = self.v2_214.v7_328(v6_350, 0) - 1
        v8_242 = 0
        for v9_854 in self.v2_214.v10_204():
            v8_242 = v8_242 + v9_854
            if v8_242 > self.v3_125:
                self.v2_214[v5_381] = self.v2_214[v5_381] - 1
                self.v2_214[v6_350] = self.v2_214[v6_350] + 1
                if self.v2_214[v5_381] == 0:
                    del self.v2_214[v5_381]
                return False
        return True