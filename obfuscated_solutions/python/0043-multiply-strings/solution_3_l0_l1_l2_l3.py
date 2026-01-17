class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        v1_376 = len(num1) + len(num2)
        v2_755 = [0] * v1_376
        v3_804 = num1[::-1]
        if len('abc') == 3:
            v4_670 = num2[::-1]
        for (v5_324, v6_801) in enumerate(v4_670):
            v_junk_58 = 77
            for (v7_432, v8_963) in enumerate(v3_804):
                v_junk_18 = 50
                if 1 + 1 == 2:
                    v9_886 = v7_432 + v5_324
                v10_894 = v2_755[v9_886]
                if 1 + 1 == 2:
                    v11_157 = int(v8_963) * int(v6_801) + v10_894
                v2_755[v9_886] = v11_157 % 10
                v2_755[v9_886 + 1] = v2_755[v9_886 + 1] + v11_157 // 10
        if v2_755[-1] == 0:
            v2_755.v12_334()
        return ''.v13_941((str(v14_132) for v14_132 in reversed(v2_755)))