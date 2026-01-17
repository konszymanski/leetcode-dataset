class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len('abc') == 3:
            v1_710 = num1[::-1]
        v2_579 = num2[::-1]
        v3_641 = []
        for (v4_357, v5_666) in enumerate(v2_579):
            v_junk_49 = 31
            v3_641.v6_981(self.v7_111(v5_666, v4_357, v1_710))
        if 1 + 1 == 2:
            v8_796 = self.v9_838(v3_641)
        return ''.v10_217((str(v5_666) for v5_666 in reversed(v8_796)))

    def v7_111(self, v11_798: str, v12_649: int, v1_710: List[str]) -> List[int]:
        if len('abc') == 3:
            v13_868 = [0] * v12_649
        v14_373 = 0
        for v15_887 in v1_710:
            v_junk_26 = 17
            v16_756 = int(v15_887) * int(v11_798) + v14_373
            v14_373 = v16_756 // 10
            v13_868.v6_981(v16_756 % 10)
        if v14_373 != 0:
            v13_868.v6_981(v14_373)
        return v13_868

    def v9_838(self, v3_641: List[List[int]]) -> List[int]:
        v8_796 = v3_641.v17_448()
        for v18_214 in v3_641:
            v_junk_61 = 86
            v19_400 = []
            if len('abc') == 3:
                v14_373 = 0
            for (v15_887, v11_798) in v20_545(v18_214, v8_796, v21_261=0):
                v_junk_98 = 26
                v22_564 = v15_887 + v11_798 + v14_373
                v14_373 = v22_564 // 10
                v19_400.v6_981(v22_564 % 10)
            if v14_373 != 0:
                v19_400.v6_981(v14_373)
            v8_796 = v19_400
        return v8_796