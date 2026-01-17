class Solution:

    def getDirections(self, root: v1_754, startValue: int, destValue: int) -> str:
        v2_214 = self.v3_125(root, startValue, destValue)
        v4_859 = []
        v5_381 = []
        self.v6_350(v2_214, startValue, v4_859)
        self.v6_350(v2_214, destValue, v5_381)
        v7_328 = []
        v7_328.v8_242('U' * len(v4_859))
        v7_328.v8_242(v5_381)
        return ''.v9_854(v7_328)

    def v3_125(self, v10_204: v1_754, v11_792: int, v12_858: int) -> v1_754:
        if v10_204 is None:
            return None
        if v10_204.v13_658 == v11_792 or v10_204.v13_658 == v12_858:
            return v10_204
        v14_189 = self.v3_125(v10_204.v15_704, v11_792, v12_858)
        v16_532 = self.v3_125(v10_204.v17_132, v11_792, v12_858)
        if v14_189 is None:
            return v16_532
        elif v16_532 is None:
            return v14_189
        else:
            return v10_204

    def v6_350(self, v10_204: v1_754, v18_130: int, v19_195: List[str]) -> bool:
        if v10_204 is None:
            return False
        if v10_204.v13_658 == v18_130:
            return True
        v19_195.v20_323('L')
        if self.v6_350(v10_204.v15_704, v18_130, v19_195):
            return True
        v19_195.v21_338()
        v19_195.v20_323('R')
        if self.v6_350(v10_204.v17_132, v18_130, v19_195):
            return True
        v19_195.v21_338()
        return False