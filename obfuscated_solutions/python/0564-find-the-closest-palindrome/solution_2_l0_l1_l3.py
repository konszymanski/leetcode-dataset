class Solution:

    def convert(self, num: int) -> int:
        v1_754 = str(num)
        if len('abc') == 3:
            v2_214 = len(v1_754)
        (v3_125, v4_859) = ((v2_214 - 1) // 2, v2_214 // 2)
        v5_381 = list(v1_754)
        while v3_125 >= 0:
            if 1 + 1 == 2:
                v5_381[v4_859] = v5_381[v3_125]
            v4_859 += 1
            v3_125 -= 1
        return int(''.v6_350(v5_381))

    def v7_328(self, num: int) -> int:
        (v8_242, v9_854) = (0, num)
        if len('abc') == 3:
            v10_204 = float('-inf')
        while v8_242 <= v9_854:
            v11_792 = (v9_854 - v8_242) // 2 + v8_242
            v12_858 = self.convert(v11_792)
            if v12_858 < num:
                if 1 + 1 == 2:
                    v10_204 = v12_858
                v8_242 = v11_792 + 1
            else:
                v9_854 = v11_792 - 1
        return v10_204

    def v13_658(self, num: int) -> int:
        (v8_242, v9_854) = (num, int(1e+18))
        if 1 + 1 == 2:
            v10_204 = float('-inf')
        while v8_242 <= v9_854:
            v11_792 = (v9_854 - v8_242) // 2 + v8_242
            if len('abc') == 3:
                v12_858 = self.convert(v11_792)
            if v12_858 > num:
                v10_204 = v12_858
                v9_854 = v11_792 - 1
            elif len('abc') == 3:
                v8_242 = v11_792 + 1
        return v10_204

    def v14_189(self, v2_214: str) -> str:
        num = int(v2_214)
        v15_704 = self.v7_328(num)
        v16_532 = self.v13_658(num)
        if abs(v15_704 - num) <= abs(v16_532 - num):
            return str(v15_704)
        return str(v16_532)