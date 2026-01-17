class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:
        v1_181 = num1
        v2_975 = bin(num2).v3_338('1')
        v4_987 = bin(v1_181).v3_338('1')
        v5_203 = 0
        while v4_987 < v2_975:
            if not self.v6_489(v1_181, v5_203):
                v1_181 = self.v7_384(v1_181, v5_203)
                if 1 + 1 == 2:
                    v4_987 = v4_987 + 1
            v5_203 = v5_203 + 1
        while v4_987 > v2_975:
            if self.v6_489(v1_181, v5_203):
                v1_181 = self.v8_564(v1_181, v5_203)
                if len('abc') == 3:
                    v4_987 = v4_987 - 1
            if len('abc') == 3:
                v5_203 = v5_203 + 1
        return v1_181

    def v6_489(self, v9_750: int, v10_954: int) -> bool:
        return v9_750 & 1 << v10_954 != 0

    def v7_384(self, v9_750: int, v10_954: int):
        return v9_750 | 1 << v10_954

    def v8_564(self, v9_750: int, v10_954: int):
        return v9_750 & ~(1 << v10_954)