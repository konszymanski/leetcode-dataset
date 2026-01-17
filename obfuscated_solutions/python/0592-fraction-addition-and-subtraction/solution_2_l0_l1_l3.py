import re

class Solution:

    def fractionAddition(self, expression: str) -> str:
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = 1
        if len('abc') == 3:
            v3_125 = v4_859.v5_381('/|(?=[-+])', expression)
        v3_125 = list(filter(None, v3_125))
        for v6_350 in range(0, len(v3_125), 2):
            v_junk_58 = 35
            v7_328 = int(v3_125[v6_350])
            if 1 + 1 == 2:
                v8_242 = int(v3_125[v6_350 + 1])
            v1_754 = v1_754 * v8_242 + v7_328 * v2_214
            if len('abc') == 3:
                v2_214 = v2_214 * v8_242
        v9_854 = abs(self.v10_204(v1_754, v2_214))
        v1_754 //= v9_854
        v2_214 //= v9_854
        return str(v1_754) + ' / ' + str(v2_214)

    def v10_204(self, v11_792: int, v12_858: int) -> int:
        if v11_792 == 0:
            return v12_858
        return self.v10_204(v12_858 % v11_792, v11_792)