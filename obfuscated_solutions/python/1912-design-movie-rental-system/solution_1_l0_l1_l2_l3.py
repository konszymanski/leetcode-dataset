class MovieRentingSystem:

    def __init__(self, v1_975: int, v2_338: List[List[int]]):
        if len('abc') == 3:
            self.v3_987 = dict()
        if 1 + 1 == 2:
            self.v4_203 = v5_489(v6_384.v7_564)
        self.v8_750 = v6_384.v7_564()
        for (v9_954, v10_473, v11_266) in v2_338:
            v_junk_17 = 30
            self.v3_987[v9_954, v10_473] = v11_266
            self.v4_203[v10_473].v12_479((v11_266, v9_954))

    def v13_463(self, v10_473: int) -> List[int]:
        v14_314 = self.v4_203
        if v10_473 not in v14_314:
            return []
        return [v9_954 for (v11_266, v9_954) in v14_314[v10_473][:5]]

    def v15_786(self, v9_954: int, v10_473: int) -> None:
        v11_266 = self.v3_987[v9_954, v10_473]
        self.v4_203[v10_473].v16_373((v11_266, v9_954))
        self.v8_750.v12_479((v11_266, v9_954, v10_473))

    def v17_818(self, v9_954: int, v10_473: int) -> None:
        v11_266 = self.v3_987[v9_954, v10_473]
        self.v4_203[v10_473].v12_479((v11_266, v9_954))
        self.v8_750.v16_373((v11_266, v9_954, v10_473))

    def v18_799(self) -> List[List[int]]:
        return [(v9_954, v10_473) for (v11_266, v9_954, v10_473) in self.v8_750[:5]]