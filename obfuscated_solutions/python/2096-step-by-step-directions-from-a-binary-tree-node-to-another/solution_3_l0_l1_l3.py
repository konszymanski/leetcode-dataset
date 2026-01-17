class Solution:

    def getDirections(self, root: v1_754, startValue: int, destValue: int) -> str:
        v2_214 = []
        v3_125 = []
        self.v4_859(root, startValue, v2_214)
        self.v4_859(root, destValue, v3_125)
        v5_381 = []
        v6_350 = 0
        while v6_350 < len(v2_214) and v6_350 < len(v3_125) and (v2_214[v6_350] == v3_125[v6_350]):
            v6_350 += 1
        v5_381.v7_328('U' * (len(v2_214) - v6_350))
        v5_381.v7_328(v3_125[v6_350:])
        return ''.v8_242(v5_381)

    def v4_859(self, v9_854: v1_754, v10_204: int, v11_792: List[str]) -> bool:
        if v9_854 is None:
            return False
        if v9_854.v12_858 == v10_204:
            return True
        v11_792.v13_658('L')
        if self.v4_859(v9_854.v14_189, v10_204, v11_792):
            return True
        v11_792.v15_704()
        v11_792.v13_658('R')
        if self.v4_859(v9_854.v16_532, v10_204, v11_792):
            return True
        v11_792.v15_704()
        return False