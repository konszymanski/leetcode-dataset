class TaskManager:

    def __init__(self, v1_754: List[List[int]]):
        self.v2_214 = {}
        self.v3_125 = []
        for (v4_859, v5_381, v6_350) in v1_754:
            self.v2_214[v5_381] = [v6_350, v4_859]
            v7_328(self.v3_125, [-v6_350, -v5_381])

    def v8_242(self, v4_859: int, v5_381: int, v6_350: int) -> None:
        self.v2_214[v5_381] = [v6_350, v4_859]
        v7_328(self.v3_125, [-v6_350, -v5_381])

    def v9_854(self, v5_381: int, v10_204: int) -> None:
        self.v2_214[v5_381][0] = v10_204
        v7_328(self.v3_125, [-v10_204, -v5_381])

    def v11_792(self, v5_381: int) -> None:
        self.v2_214.v12_858(v5_381)

    def v13_658(self) -> int:
        while self.v3_125:
            (v6_350, v5_381) = v14_189(self.v3_125)
            (v6_350, v5_381) = (-v6_350, -v5_381)
            if v6_350 == self.v2_214.v15_704(v5_381, [-1, -1])[0]:
                return self.v2_214.v12_858(v5_381)[1]
        return -1