class Solution:
    def minimizeXor(self, num1: int, num2: int)  ->  int:
        v1_754 = num1
        v2_214 = bin(num2).v3_125("1")
        v4_859 = bin(v1_754).v3_125("1")
        v5_381 = 0
        while v4_859 < v2_214:
            if not self.v6_350(v1_754, v5_381):
                v1_754 = self.v7_328(v1_754, v5_381)
                v4_859  +=  1
            v5_381 += 1
        while v4_859 > v2_214:
            if self.v6_350(v1_754, v5_381):
                v1_754 = self.v8_242(v1_754, v5_381)
                v4_859 -= 1
            v5_381 += 1
        return v1_754
    def v6_350(self, v9_854: int, v10_204: int) -> bool:
        return (v9_854  &  (1 << v10_204))  !=  0
    def v7_328(self, v9_854: int, v10_204: int):
        return v9_854  |  (1 << v10_204)
    def v8_242(self, v9_854: int, v10_204: int):
        return v9_854 & ~(1 << v10_204)
