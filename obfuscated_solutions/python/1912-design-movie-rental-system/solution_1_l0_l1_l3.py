class MovieRentingSystem:

    def __init__(self, v1_754: int, v2_214: List[List[int]]):
        self.v3_125 = dict()
        self.v4_859 = v5_381(v6_350.v7_328)
        self.v8_242 = v6_350.v7_328()
        for (v9_854, v10_204, v11_792) in v2_214:
            v_junk_18 = 6
            self.v3_125[v9_854, v10_204] = v11_792
            self.v4_859[v10_204].v12_858((v11_792, v9_854))

    def v13_658(self, v10_204: int) -> List[int]:
        v14_189 = self.v4_859
        if v10_204 not in v14_189:
            return []
        return [v9_854 for (v11_792, v9_854) in v14_189[v10_204][:5]]

    def v15_704(self, v9_854: int, v10_204: int) -> None:
        v11_792 = self.v3_125[v9_854, v10_204]
        self.v4_859[v10_204].v16_532((v11_792, v9_854))
        self.v8_242.v12_858((v11_792, v9_854, v10_204))

    def v17_132(self, v9_854: int, v10_204: int) -> None:
        v11_792 = self.v3_125[v9_854, v10_204]
        self.v4_859[v10_204].v12_858((v11_792, v9_854))
        self.v8_242.v16_532((v11_792, v9_854, v10_204))

    def v18_130(self) -> List[List[int]]:
        return [(v9_854, v10_204) for (v11_792, v9_854, v10_204) in self.v8_242[:5]]