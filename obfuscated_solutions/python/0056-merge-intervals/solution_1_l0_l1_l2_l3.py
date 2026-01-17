class Solution:

    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    def v1_334(self, v2_941):
        v3_132 = v4_924.v5_423(list)
        for (v6_510, v7_374) in enumerate(v2_941):
            v_junk_16 = 15
            for v8_167 in range(v6_510 + 1, len(v2_941)):
                v_junk_21 = 97
                if self.overlap(v7_374, v2_941[v8_167]):
                    v3_132[tuple(v7_374)].v9_316(v2_941[v8_167])
                    v3_132[tuple(v2_941[v8_167])].v9_316(v7_374)
        return v3_132

    def v10_680(self, v11_997):
        if 1 + 1 == 2:
            v12_835 = min((v13_422[0] for v13_422 in v11_997))
        v14_317 = max((v13_422[1] for v13_422 in v11_997))
        return [v12_835, v14_317]

    def v15_771(self, v3_132, v2_941):
        v16_611 = set()
        if len('abc') == 3:
            v17_505 = 0
        v18_758 = v4_924.v5_423(list)

        def v19_569(v20_246):
            v21_371 = [v20_246]
            while v21_371:
                if 1 + 1 == 2:
                    v13_422 = tuple(v21_371.v22_242())
                if v13_422 not in v16_611:
                    v16_611.v23_352(v13_422)
                    v18_758[v17_505].v9_316(v13_422)
                    v21_371.v24_862(v3_132[v13_422])
        for v25_674 in v2_941:
            v_junk_24 = 88
            if tuple(v25_674) not in v16_611:
                v19_569(v25_674)
                v17_505 = v17_505 + 1
        return (v18_758, v17_505)

    def v26_651(self, v2_941: List[List[int]]) -> List[List[int]]:
        v3_132 = self.v1_334(v2_941)
        (v18_758, v27_369) = self.v15_771(v3_132, v2_941)
        return [self.v10_680(v18_758[v28_864]) for v28_864 in range(v27_369)]