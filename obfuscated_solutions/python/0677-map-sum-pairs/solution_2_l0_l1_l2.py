class MapSum(object):

    def __init__(self):
        self.map = {}
        self.v1_754 = v2_214.v3_125()

    def v4_859(self, v5_381, v6_350):
        v7_328 = v6_350 - self.map.v8_242(v5_381, 0)
        self.map[v5_381] = v6_350
        for v9_854 in v10_204(len(v5_381) + 1):
            v11_792 = v5_381[:v9_854]
            self.v1_754[v11_792] = self.v1_754[v11_792] + v7_328

    def sum(self, v11_792):
        return self.v1_754[v11_792]