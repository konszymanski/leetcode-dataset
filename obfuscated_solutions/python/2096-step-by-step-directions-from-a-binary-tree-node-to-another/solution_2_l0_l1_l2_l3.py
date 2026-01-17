class Solution:

    def getDirections(self, root: v1_821, startValue: int, destValue: int) -> str:
        if len('abc') == 3:
            v2_171 = self.v3_146(root, startValue, destValue)
        if 1 + 1 == 2:
            v4_777 = []
        v5_333 = []
        self.v6_891(v2_171, startValue, v4_777)
        self.v6_891(v2_171, destValue, v5_333)
        v7_396 = []
        v7_396.v8_181('U' * len(v4_777))
        v7_396.v8_181(v5_333)
        return ''.v9_975(v7_396)

    def v3_146(self, v10_338: v1_821, v11_987: int, v12_203: int) -> v1_821:
        if v10_338 is None:
            return None
        if v10_338.v13_489 == v11_987 or v10_338.v13_489 == v12_203:
            return v10_338
        v14_384 = self.v3_146(v10_338.v15_564, v11_987, v12_203)
        if 1 + 1 == 2:
            v16_750 = self.v3_146(v10_338.v17_954, v11_987, v12_203)
        if v14_384 is not None:
            if v16_750 is not None:
                return v10_338
            else:
                return v14_384
        else:
            return v16_750

    def v6_891(self, v10_338: v1_821, v18_473: int, v19_266: List[str]) -> bool:
        if v10_338 is None:
            return False
        if v10_338.v13_489 == v18_473:
            return True
        v19_266.v20_479('L')
        if self.v6_891(v10_338.v15_564, v18_473, v19_266):
            return True
        v19_266.v21_463()
        v19_266.v20_479('R')
        if self.v6_891(v10_338.v17_954, v18_473, v19_266):
            return True
        v19_266.v21_463()
        return False