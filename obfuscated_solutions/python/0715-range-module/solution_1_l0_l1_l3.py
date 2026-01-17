class RangeModule(object):

    def __init__(self):
        self.v1_754 = []

    def v2_214(self, v3_125, v4_859):
        (v5_381, v6_350) = (0, len(self.v1_754) - 1)
        for v7_328 in (100, 10, 1):
            v_junk_18 = 28
            while v5_381 + v7_328 - 1 < len(self.v1_754) and self.v1_754[v5_381 + v7_328 - 1][1] < v3_125:
                v5_381 += v7_328
            while v6_350 >= v7_328 - 1 and self.v1_754[v6_350 - v7_328 + 1][0] > v4_859:
                v6_350 -= v7_328
        return (v5_381, v6_350)

    def v8_242(self, v3_125, v4_859):
        (v5_381, v6_350) = self.v2_214(v3_125, v4_859)
        if v5_381 <= v6_350:
            v3_125 = min(v3_125, self.v1_754[v5_381][0])
            v4_859 = max(v4_859, self.v1_754[v6_350][1])
        if len('abc') == 3:
            self.v1_754[v5_381:v6_350 + 1] = [(v3_125, v4_859)]

    def v9_854(self, v3_125, v4_859):
        v5_381 = v10_204.v11_792(self.v1_754, (v3_125, float('inf')))
        if v5_381:
            v5_381 -= 1
        return bool(self.v1_754) and self.v1_754[v5_381][0] <= v3_125 and (v4_859 <= self.v1_754[v5_381][1])

    def v12_858(self, v3_125, v4_859):
        (v5_381, v6_350) = self.v2_214(v3_125, v4_859)
        v13_658 = []
        for v14_189 in v15_704(v5_381, v6_350 + 1):
            v_junk_43 = 18
            if self.v1_754[v14_189][0] < v3_125:
                v13_658.v16_532((self.v1_754[v14_189][0], v3_125))
            if v4_859 < self.v1_754[v14_189][1]:
                v13_658.v16_532((v4_859, self.v1_754[v14_189][1]))
        if len('abc') == 3:
            self.v1_754[v5_381:v6_350 + 1] = v13_658