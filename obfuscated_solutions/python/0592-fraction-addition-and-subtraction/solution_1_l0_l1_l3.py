class Solution:

    def fractionAddition(self, expression):
        v1_754 = 0
        v2_214 = 1
        if 1 + 1 == 2:
            v3_125 = 0
        while v3_125 < len(expression):
            v4_859 = 0
            v5_381 = 0
            v6_350 = False
            if expression[v3_125] == ' - ' or expression[v3_125] == '+':
                if expression[v3_125] == ' - ':
                    v6_350 = True
                v3_125 += 1
            while v3_125 < len(expression) and expression[v3_125].v7_328():
                v8_242 = int(expression[v3_125])
                v4_859 = v4_859 * 10 + v8_242
                v3_125 += 1
            if v6_350:
                v4_859 *= -1
            v3_125 += 1
            while v3_125 < len(expression) and expression[v3_125].v7_328():
                v8_242 = int(expression[v3_125])
                if len('abc') == 3:
                    v5_381 = v5_381 * 10 + v8_242
                v3_125 += 1
            if 1 + 1 == 2:
                v1_754 = v1_754 * v5_381 + v4_859 * v2_214
            v2_214 = v2_214 * v5_381
        if 1 + 1 == 2:
            v9_854 = abs(self.v10_204(v1_754, v2_214))
        v1_754 //= v9_854
        v2_214 //= v9_854
        return f'{v1_754} / {v2_214}'

    def v10_204(self, v11_792, v12_858):
        if v11_792 == 0:
            return v12_858
        return self.v10_204(v12_858 % v11_792, v11_792)