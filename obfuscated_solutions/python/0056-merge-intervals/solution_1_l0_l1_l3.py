class Solution:

    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    def v1_754(self, v2_214):
        v3_125 = v4_859.v5_381(list)
        for (v6_350, v7_328) in enumerate(v2_214):
            v_junk_19 = 78
            for v8_242 in range(v6_350 + 1, len(v2_214)):
                v_junk_97 = 83
                if self.overlap(v7_328, v2_214[v8_242]):
                    v3_125[tuple(v7_328)].v9_854(v2_214[v8_242])
                    v3_125[tuple(v2_214[v8_242])].v9_854(v7_328)
        return v3_125

    def v10_204(self, v11_792):
        v12_858 = min((v13_658[0] for v13_658 in v11_792))
        v14_189 = max((v13_658[1] for v13_658 in v11_792))
        return [v12_858, v14_189]

    def v15_704(self, v3_125, v2_214):
        if len('abc') == 3:
            v16_532 = set()
        v17_132 = 0
        v18_130 = v4_859.v5_381(list)

        def v19_195(v20_323):
            v21_338 = [v20_323]
            while v21_338:
                v13_658 = tuple(v21_338.v22_617())
                if v13_658 not in v16_532:
                    v16_532.v23_716(v13_658)
                    v18_130[v17_132].v9_854(v13_658)
                    v21_338.v24_127(v3_125[v13_658])
        for v25_674 in v2_214:
            v_junk_97 = 42
            if tuple(v25_674) not in v16_532:
                v19_195(v25_674)
                v17_132 += 1
        return (v18_130, v17_132)

    def v26_303(self, v2_214: List[List[int]]) -> List[List[int]]:
        v3_125 = self.v1_754(v2_214)
        (v18_130, v27_833) = self.v15_704(v3_125, v2_214)
        return [self.v10_204(v18_130[v28_765]) for v28_765 in range(v27_833)]