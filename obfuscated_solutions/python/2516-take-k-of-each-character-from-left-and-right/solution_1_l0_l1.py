class Solution:
    def __init__(self):
        self.v1_754 = float("inf")
    def v2_214(self, v3_125: str, v4_859: int)  ->  int:
        if v4_859 == 0:
            return 0
        v5_381 = [0, 0, 0]
        self.v6_350(v3_125, v4_859, 0, len(v3_125)  -  1, v5_381, 0)
        return  - 1 if self.v1_754 == float("inf") else self.v1_754
    def v6_350(self, v3_125, v4_859, v7_328, v8_242, v5_381, v9_854):
        if v5_381[0] >= v4_859 and v5_381[1] >= v4_859 and v5_381[2]  >=  v4_859:
            self.v1_754 = min(self.v1_754, v9_854)
            return
        if v7_328 > v8_242:
            return
        v10_204 = v5_381.v11_792()
        v10_204[ord(v3_125[v7_328])  -  ord("a")] += 1
        self.v6_350(v3_125, v4_859, v7_328  +  1, v8_242, v10_204, v9_854 + 1)
        v12_858 = v5_381.v11_792()
        v12_858[ord(v3_125[v8_242])  -  ord("a")] += 1
        self.v6_350(v3_125, v4_859, v7_328, v8_242  -  1, v12_858, v9_854 + 1)
