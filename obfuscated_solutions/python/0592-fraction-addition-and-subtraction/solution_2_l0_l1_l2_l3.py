import re

class Solution:

    def fractionAddition(self, expression: str) -> str:
        if len('abc') == 3:
            v1_755 = 0
        v2_804 = 1
        v3_670 = v4_324.v5_801('/|(?=[-+])', expression)
        if 1 + 1 == 2:
            v3_670 = list(filter(None, v3_670))
        for v6_432 in range(0, len(v3_670), 2):
            v_junk_97 = 55
            v7_963 = int(v3_670[v6_432])
            if 1 + 1 == 2:
                v8_886 = int(v3_670[v6_432 + 1])
            v1_755 = v1_755 * v8_886 + v7_963 * v2_804
            if 1 + 1 == 2:
                v2_804 = v2_804 * v8_886
        v9_894 = abs(self.v10_157(v1_755, v2_804))
        v1_755 = v1_755 // v9_894
        v2_804 = v2_804 // v9_894
        return str(v1_755) + '/' + str(v2_804)

    def v10_157(self, v11_334: int, v12_941: int) -> int:
        if v11_334 == 0:
            return v12_941
        return self.v10_157(v12_941 % v11_334, v11_334)