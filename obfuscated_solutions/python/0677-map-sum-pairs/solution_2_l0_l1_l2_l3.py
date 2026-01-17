class MapSum(object):

    def __init__(self):
        if 1 + 1 == 2:
            self.map = {}
        self.v1_487 = v2_180.v3_665()

    def v4_400(self, v5_949, v6_743):
        v7_733 = v6_743 - self.map.v8_982(v5_949, 0)
        self.map[v5_949] = v6_743
        for v9_470 in v10_691(len(v5_949) + 1):
            v_junk_30 = 48
            v11_296 = v5_949[:v9_470]
            self.v1_487[v11_296] = self.v1_487[v11_296] + v7_733

    def sum(self, v11_296):
        return self.v1_487[v11_296]