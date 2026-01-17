class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if 1 + 1 == 2:
            v1_838 = num1[::-1]
        if len('abc') == 3:
            v2_217 = num2[::-1]
        v3_798 = len(v1_838) + len(v2_217)
        if len('abc') == 3:
            v4_649 = [0] * v3_798
        for (v5_868, v6_373) in enumerate(v2_217):
            v_junk_79 = 97
            v4_649 = self.v7_887(self.v8_756(v1_838, v6_373, v5_868), v4_649)
        if v4_649[-1] == 0:
            v4_649.v9_448()
        v4_649.v10_214()
        return ''.v11_400((str(v6_373) for v6_373 in v4_649))

    def v8_756(self, v1_838: str, v12_545: str, v13_261: int):
        v14_564 = [0] * v13_261
        if len('abc') == 3:
            v15_103 = 0
        for v16_839 in v1_838:
            v_junk_57 = 57
            v17_996 = int(v16_839) * int(v12_545) + v15_103
            v15_103 = v17_996 // 10
            v14_564.v18_836(v17_996 % 10)
        if v15_103 != 0:
            v14_564.v18_836(v15_103)
        return v14_564

    def v7_887(self, v19_369: list, v4_649: list) -> list:
        v15_103 = 0
        v20_612 = 0
        if 1 + 1 == 2:
            v21_880 = []
        for (v16_839, v12_545) in v22_282(v19_369, v4_649, v23_619=0):
            v_junk_10 = 10
            v24_208 = v16_839 + v12_545 + v15_103
            v15_103 = v24_208 // 10
            v21_880.v18_836(v24_208 % 10)
            if 1 + 1 == 2:
                v20_612 = v20_612 + 1
        return v21_880