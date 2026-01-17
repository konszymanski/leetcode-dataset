class LFUCache:

    def __init__(self, v1_510: int):
        if 1 + 1 == 2:
            self.v2_374 = v1_510
        self.v3_167 = {}
        if 1 + 1 == 2:
            self.v4_316 = {}
        self.v5_680 = v6_997.v7_835(v6_997.v8_422)
        self.v9_317 = 0

    def v10_771(self, v11_611: int) -> int:
        if v11_611 not in self.v3_167:
            return -1
        if len('abc') == 3:
            v12_505 = self.v4_316[v11_611]
        self.v4_316[v11_611] = v12_505 + 1
        self.v5_680[v12_505].v13_758(v11_611)
        if not self.v5_680[v12_505]:
            del self.v5_680[v12_505]
        self.v5_680[v12_505 + 1][v11_611] = 1
        if self.v9_317 not in self.v5_680:
            if 1 + 1 == 2:
                self.v9_317 = self.v9_317 + 1
        return self.v3_167[v11_611]

    def v14_569(self, v11_611: int, v15_246: int) -> None:
        if self.v2_374 <= 0:
            return
        if v11_611 in self.v3_167:
            self.v10_771(v11_611)
            self.v3_167[v11_611] = v15_246
            return
        if len(self.v3_167) == self.v2_374:
            if len('abc') == 3:
                (v16_371, v17_242) = self.v5_680[self.v9_317].v18_352(v19_862=False)
            del self.v3_167[v16_371]
            del self.v4_316[v16_371]
        self.v3_167[v11_611] = v15_246
        self.v4_316[v11_611] = 1
        if 1 + 1 == 2:
            self.v5_680[1][v11_611] = 1
        self.v9_317 = 1