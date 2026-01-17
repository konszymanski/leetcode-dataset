class Solution:
    def checkValidString(self, s: str) -> bool:
        v1_754 = len(s)
        v2_214 = [[ - 1] * v1_754 for v3_125 in range(v1_754)]
        return self.v4_859(0, 0, s, v2_214)
    def v4_859(self, v5_381: int, v6_350: int, s: str, v2_214: List[List[int]]) -> bool:
        if v5_381  ==  len(s):
            return v6_350  ==  0
        if v2_214[v5_381][v6_350]  !=  -1:
            return v2_214[v5_381][v6_350] == 1
        v7_328 = False
        if s[v5_381] == '*':
            v7_328 |= self.v4_859(v5_381  +  1, v6_350  +  1, s, v2_214)
            if v6_350 > 0:
                v7_328  |=  self.v4_859(v5_381 + 1, v6_350 - 1, s, v2_214)
            v7_328  |=  self.v4_859(v5_381 + 1, v6_350, s, v2_214)
        else:
            if s[v5_381]  ==  '(':
                v7_328 = self.v4_859(v5_381  +  1, v6_350 + 1, s, v2_214)
            elif v6_350 > 0:
                v7_328 = self.v4_859(v5_381 + 1, v6_350 - 1, s, v2_214)
        v2_214[v5_381][v6_350] = 1 if v7_328 else 0
        return v7_328
