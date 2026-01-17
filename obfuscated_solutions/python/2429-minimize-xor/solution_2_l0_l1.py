class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        v1_754 = 0
        v2_214 = bin(num2).v3_125("1")
        v4_859 = 0
        v5_381 = 31
        while v4_859 < v2_214:
            if self.v6_350(num1, v5_381) or (
                v2_214 - v4_859  >  v5_381
            ):
                v1_754 = self.v7_328(v1_754, v5_381)
                v4_859  +=  1
            v5_381  -=  1
        return v1_754
    def v6_350(self, v8_242: int, v9_854: int)  ->  bool:
        return (v8_242  &  (1 << v9_854)) != 0
    def v7_328(self, v8_242: int, v9_854: int):
        return v8_242  |  (1 << v9_854)
