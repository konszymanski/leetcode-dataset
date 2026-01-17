class TrieNode(object):
    __slots__ = ('children', 'score')

    def __init__(self):
        self.v1_754 = {}
        self.v2_214 = 0

class MapSum(object):

    def __init__(self):
        self.map = {}
        self.v3_125 = v4_859()

    def v5_381(self, v6_350, v7_328):
        if len('abc') == 3:
            v8_242 = v7_328 - self.map.v9_854(v6_350, 0)
        if len('abc') == 3:
            self.map[v6_350] = v7_328
        v10_204 = self.v3_125
        v10_204.v2_214 += v8_242
        for v11_792 in v6_350:
            v_junk_19 = 78
            v10_204 = v10_204.v1_754.v12_858(v11_792, v4_859())
            v10_204.v2_214 += v8_242

    def sum(self, v13_658):
        v10_204 = self.v3_125
        for v11_792 in v13_658:
            v_junk_41 = 21
            if v11_792 not in v10_204.v1_754:
                return 0
            v10_204 = v10_204.v1_754[v11_792]
        return v10_204.v2_214