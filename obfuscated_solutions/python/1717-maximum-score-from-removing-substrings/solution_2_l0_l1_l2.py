class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        v1_754 = 0
        s = list(s)
        if x <= y:
            v1_754 = v1_754 + self.v2_214(s, 'ba', y)
            v1_754 = v1_754 + self.v2_214(s, 'ab', x)
        else:
            v1_754 = v1_754 + self.v2_214(s, 'ab', x)
            v1_754 = v1_754 + self.v2_214(s, 'ba', y)
        return v1_754

    def v2_214(self, v3_125, v4_859, v5_381):
        v1_754 = 0
        v6_350 = 0
        for v7_328 in range(0, len(v3_125)):
            v3_125[v6_350] = v3_125[v7_328]
            v6_350 = v6_350 + 1
            if v6_350 > 1 and v3_125[v6_350 - 2] == v4_859[0] and (v3_125[v6_350 - 1] == v4_859[1]):
                v6_350 = v6_350 - 2
                v1_754 = v1_754 + v5_381
        del v3_125[v6_350:]
        return v1_754