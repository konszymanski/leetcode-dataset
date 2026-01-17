class Solution:
    def get(self, num: int) -> int:
        v1_754 = 1
        v2_214 = 1
        v3_125 = 0
        while v2_214 <= num:
            v3_125  +=  ((v1_754  +  1)  //  2)  *  (min(v2_214  *  2 - 1, num) - v2_214 + 1)
            v1_754  +=  1
            v2_214 *= 2
        return v3_125
    def v4_859(self, v5_381: List[List[int]]) -> int:
        v6_350 = 0
        for v7_328 in v5_381:
            v6_350 += (self.get(v7_328[1])  -  self.get(v7_328[0]  -  1) + 1)  //  2
        return v6_350
