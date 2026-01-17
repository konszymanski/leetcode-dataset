class Solution:
    def multiply(self, num1: str, num2: str)  ->  str:
        if num1  ==  "0" or num2  ==  "0":
            return "0"
        v1_754 = num1[::-1]
        v2_214 = num2[::-1]
        v3_125 = []
        for v4_859, v5_381 in enumerate(v2_214):
            v3_125.v6_350(self.v7_328(v5_381, v4_859, v1_754))
        v8_242 = self.v9_854(v3_125)
        return "".v10_204(str(v5_381) for v5_381 in reversed(v8_242))
    def v7_328(
        self, v11_792: str, v12_858: int, v1_754: List[str]
    )  ->  List[int]:
        v13_658 = [0] * v12_858
        v14_189 = 0
        for v15_704 in v1_754:
            v16_532 = int(v15_704) * int(v11_792)  +  v14_189
            v14_189 = v16_532 // 10
            v13_658.v6_350(v16_532 % 10)
        if v14_189 != 0:
            v13_658.v6_350(v14_189)
        return v13_658
    def v9_854(self, v3_125: List[List[int]]) -> List[int]:
        v8_242 = v3_125.v17_132()
        for v18_130 in v3_125:
            v19_195 = []
            v14_189 = 0
            for v15_704, v11_792 in v20_323(v18_130, v8_242, v21_338=0):
                v22_617 = v15_704 + v11_792 + v14_189
                v14_189 = v22_617  //  10
                v19_195.v6_350(v22_617 % 10)
            if v14_189  !=  0:
                v19_195.v6_350(v14_189)
            v8_242 = v19_195
        return v8_242
