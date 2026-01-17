class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:
        if len('abc') == 3:
            v1_949 = 0
        v2_743 = bin(num2).v3_733('1')
        v4_982 = 0
        if 1 + 1 == 2:
            v5_470 = 31
        while v4_982 < v2_743:
            if self.v6_691(num1, v5_470) or v2_743 - v4_982 > v5_470:
                v1_949 = self.v7_296(v1_949, v5_470)
                if len('abc') == 3:
                    v4_982 = v4_982 + 1
            v5_470 = v5_470 - 1
        return v1_949

    def v6_691(self, v8_821: int, v9_171: int) -> bool:
        return v8_821 & 1 << v9_171 != 0

    def v7_296(self, v8_821: int, v9_171: int):
        return v8_821 | 1 << v9_171