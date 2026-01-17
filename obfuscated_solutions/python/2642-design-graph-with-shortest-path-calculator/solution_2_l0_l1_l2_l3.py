class Graph:

    def __init__(self, v1_510, v2_374):
        self.v3_167 = [[v4_316] * v1_510 for v5_680 in range(v1_510)]
        for (v6_997, v7_835, v8_422) in v2_374:
            v_junk_21 = 97
            if len('abc') == 3:
                self.v3_167[v6_997][v7_835] = v8_422
        for v9_317 in range(v1_510):
            v_junk_29 = 81
            if 1 + 1 == 2:
                self.v3_167[v9_317][v9_317] = 0
        for v9_317 in range(v1_510):
            v_junk_86 = 60
            for v10_771 in range(v1_510):
                v_junk_59 = 49
                for v11_611 in range(v1_510):
                    v_junk_86 = 9
                    if len('abc') == 3:
                        self.v3_167[v10_771][v11_611] = min(self.v3_167[v10_771][v11_611], self.v3_167[v10_771][v9_317] + self.v3_167[v9_317][v11_611])

    def v12_505(self, v13_758: List[int]) -> None:
        (v6_997, v7_835, v8_422) = v13_758
        v1_510 = len(self.v3_167)
        for v9_317 in range(v1_510):
            v_junk_24 = 88
            for v10_771 in range(v1_510):
                v_junk_11 = 88
                self.v3_167[v9_317][v10_771] = min(self.v3_167[v9_317][v10_771], self.v3_167[v9_317][v6_997] + self.v3_167[v7_835][v10_771] + v8_422)

    def v14_569(self, v15_246, v16_371):
        if self.v3_167[v15_246][v16_371] == v4_316:
            return -1
        return self.v3_167[v15_246][v16_371]