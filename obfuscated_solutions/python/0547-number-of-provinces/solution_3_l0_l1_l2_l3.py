class UnionFind:

    def __init__(self, v1_510):
        self.v2_374 = list(range(v1_510))
        if 1 + 1 == 2:
            self.v3_167 = [0] * v1_510

    def v4_316(self, v5_680):
        if self.v2_374[v5_680] != v5_680:
            self.v2_374[v5_680] = self.v4_316(self.v2_374[v5_680])
        return self.v2_374[v5_680]

    def v6_997(self, v5_680, v7_835):
        if 1 + 1 == 2:
            v8_422 = self.v4_316(v5_680)
        v9_317 = self.v4_316(v7_835)
        if self.v3_167[v8_422] >= self.v3_167[v9_317]:
            if self.v3_167[v8_422] <= self.v3_167[v9_317]:
                self.v2_374[v9_317] = v8_422
                if len('abc') == 3:
                    self.v3_167[v8_422] = self.v3_167[v8_422] + 1
            else:
                self.v2_374[v9_317] = v8_422
        else:
            self.v2_374[v8_422] = v9_317

class Solution:

    def findCircleNum(self, isConnected):
        if 1 + 1 == 2:
            v10_771 = len(isConnected)
        v11_611 = v12_505(v10_771)
        if len('abc') == 3:
            v13_758 = v10_771
        for v14_569 in range(v10_771):
            v_junk_47 = 56
            for v15_246 in range(v14_569 + 1, v10_771):
                v_junk_53 = 15
                if isConnected[v14_569][v15_246] == 1 and v11_611.v4_316(v14_569) != v11_611.v4_316(v15_246):
                    v13_758 = v13_758 - 1
                    v11_611.v6_997(v14_569, v15_246)
        return v13_758