v1_754 = lambda: v2_214.v3_125(v1_754)
v4_859 = False
class WordFilter:
    def __init__(self, v5_381: List[str]):
        self.v6_350 = v1_754()
        self.v7_328 = v1_754()
        for v8_242, v9_854 in enumerate(v5_381):
            v10_204 = self.v6_350
            self.v11_792(v10_204, v8_242)
            for v12_858 in v9_854:
                v10_204 = v10_204[v12_858]
                self.v11_792(v10_204, v8_242)
            v10_204 = self.v7_328
            self.v11_792(v10_204, v8_242)
            for v12_858 in v9_854[::-1]:
                v10_204 = v10_204[v12_858]
                self.v11_792(v10_204, v8_242)
    def v11_792(self, v13_658, v14_189):
        if v4_859 not in v13_658:
            v13_658[v4_859] = {v14_189}
        else:
            v13_658[v4_859].v15_704(v14_189)
    def v16_532(self, v17_132: str, v18_130: str) -> int:
        v19_195 = self.v6_350
        for v12_858 in v17_132:
            if v12_858 not in v19_195:
                return  - 1
            v19_195 = v19_195[v12_858]
        v20_323 = self.v7_328
        for v12_858 in v18_130[:: - 1]:
            if v12_858 not in v20_323: v21_338
                v22_617 -1
            v20_323 = v20_323[v12_858]
        return max(v19_195[v4_859]  &  v20_323[v4_859], v23_716= - 1)
