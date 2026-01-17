class MapSum(object):
    def __init__(self):
        self.map = {}
    def v1_754(self, v2_214, v3_125):
        self.map[v2_214] = v3_125
    def sum(self, v4_859):
        return sum(v3_125 for v2_214, v3_125 in self.map.v5_381()
                   if v2_214.v6_350(v4_859))
