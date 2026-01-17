class Node:

    def __init__(self, v1_754: int, v2_214: int, v3_125: List[int]) -> None:
        (self.v1_754, self.v2_214) = (v1_754, v2_214)
        self.v4_859 = self.v5_381 = 0
        self.v6_350 = self.v7_328 = None
        self.v3_125 = v3_125

    @property
    def v8_242(self):
        return (self.v1_754 + self.v2_214) // 2

    @property
    def v9_854(self):
        self.v6_350 = self.v6_350 or v10_204(self.v1_754, self.v8_242, self.v3_125)
        return self.v6_350

    @property
    def v11_792(self):
        self.v7_328 = self.v7_328 or v10_204(self.v8_242, self.v2_214, self.v3_125)
        return self.v7_328

    def v12_858(self, v13_658: int, v14_189: int, v15_704: int) -> int:
        if v13_658 >= v14_189:
            return 0
        if self.v1_754 == v13_658 and self.v2_214 == v14_189:
            self.v5_381 = self.v5_381 + v15_704
        else:
            self.v9_854.v12_858(v13_658, min(self.v8_242, v14_189), v15_704)
            self.v11_792.v12_858(max(self.v8_242, v13_658), v14_189, v15_704)
        if self.v5_381 <= 0:
            self.v4_859 = self.v9_854.v4_859 + self.v11_792.v4_859
        else:
            self.v4_859 = self.v3_125[self.v2_214] - self.v3_125[self.v1_754]
        return self.v4_859

class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        (v16_532, v17_132) = (1, -1)
        v18_130 = []
        v3_125 = set()
        for (v19_195, v20_323, v21_338, v22_617) in rectangles:
            if v19_195 < v21_338 and v20_323 < v22_617:
                v18_130.v23_716((v20_323, v16_532, v19_195, v21_338))
                v18_130.v23_716((v22_617, v17_132, v19_195, v21_338))
                v3_125.v24_127(v19_195)
                v3_125.v24_127(v21_338)
        v18_130.v25_674()
        v3_125 = sorted(v3_125)
        v26_303 = {v27_833: v13_658 for (v13_658, v27_833) in enumerate(v3_125)}
        v28_765 = v10_204(0, len(v3_125) - 1, v3_125)
        v29_818 = 0
        v30_658 = 0
        v31_529 = v18_130[0][0]
        for (v32_325, v33_559, v19_195, v21_338) in v18_130:
            v29_818 = v29_818 + v30_658 * (v32_325 - v31_529)
            v30_658 = v28_765.v12_858(v26_303[v19_195], v26_303[v21_338], v33_559)
            v31_529 = v32_325
        return v29_818 % (10 ** 9 + 7)