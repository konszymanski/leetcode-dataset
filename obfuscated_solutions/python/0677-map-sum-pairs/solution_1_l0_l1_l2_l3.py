class MapSum(object):

    def __init__(self):
        self.map = {}

    def v1_674(self, v2_303, v3_833):
        self.map[v2_303] = v3_833

    def sum(self, v4_765):
        return sum((v3_833 for (v2_303, v3_833) in self.map.v5_818() if v2_303.v6_658(v4_765)))